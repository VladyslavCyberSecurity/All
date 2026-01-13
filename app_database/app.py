import os  # Provides functions for interacting with the operating system, like checking if files exist.
import json  # Allows converting data to and from a string format (JSON) for storage.
import base64  # Used for encoding binary data into a text format, needed for encryption keys.
from getpass import getpass  # Securely prompts for password input without showing it on screen.
from cryptography.fernet import Fernet, InvalidToken  # Fernet for encryption, InvalidToken for error handling.
from cryptography.hazmat.primitives import hashes  # Provides hash functions for key derivation.
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # Key derivation function for secure keys.
from cryptography.hazmat.backends import default_backend  # Backend for cryptographic operations.
 
class PasswordDatabase:
    """
    A class to manage an encrypted password database, like a container for all database operations.
    """
    def __init__(self, file_path, password, salt=None):
        """
        Sets up the database with a file path and password.
        If salt is None, it's a new database; otherwise, it's an existing one to load.
        """
        self.file_path = file_path  # Stores the location where the database file is saved.
        self.password = password
        if salt is None:
            # New database: generate a random 16-byte value (salt) for security.
            self.salt = os.urandom(16)
            self.entries = []  # Start with an empty list for username-password pairs with comments.
            self.key = self.derive_key()  # Create encryption key from password and salt.
            self.save()  # Save the empty database to the file.
        else:
            # Existing database: use the provided salt.
            self.salt = salt
            self.key = self.derive_key()  # Derive key for decryption.
            self.entries = self.load_entries()  # Load the encrypted data from the file.
 
    def derive_key(self):
        """
        Creates a secure encryption key from the password and salt using PBKDF2,
        which makes it hard for attackers to guess the key by trying many passwords.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),  # Uses SHA256 for hashing, a secure method.
            length=32,  # Key must be 32 bytes for Fernet.
            salt=self.salt,  # Random value to make the key unique.
            iterations=100000,  # Many iterations to slow down attackers.
            backend=default_backend()  # Uses the default cryptographic backend.
        )
        derived_key = kdf.derive(self.password.encode())  # Convert password to bytes and derive key.
        return base64.urlsafe_b64encode(derived_key)  # Encode key for Fernet compatibility.
 
    def encrypt_data(self, data):
        """
        Encrypts the given data using Fernet with the derived key,
        ensuring only someone with the key can read it.
        """
        fernet = Fernet(self.key)  # Create a Fernet instance with our key.
        return fernet.encrypt(data)  # Encrypt the data and return the encrypted bytes.
 
    def decrypt_data(self, encrypted_data):
        """
        Decrypts the given encrypted data using Fernet with the derived key,
        revealing the original data if the key is correct.
        """
        fernet = Fernet(self.key)  # Create a Fernet instance with our key.
        return fernet.decrypt(encrypted_data)  # Decrypt and return the original bytes.
 
    def save(self):
        """
        Saves the list of entries to the file by first converting to JSON,
        then encrypting it, and writing salt followed by encrypted data.
        """
        try:
            json_data = json.dumps(self.entries).encode()  # Convert list to JSON string and then to bytes.
            encrypted_data = self.encrypt_data(json_data)  # Encrypt the JSON data.
            with open(self.file_path, 'wb') as f:
                f.write(self.salt + encrypted_data)  # Write salt first, then encrypted data, in binary mode.
        except PermissionError:
            print("Permission denied. Cannot write to the file.")  # Inform user if no write permission.
        except Exception as e:
            print(f"Error saving database: {e}")  # Show any other errors during saving.
 
    def load_entries(self):
        """
        Reads and decrypts the entries from the file.
        Checks if file is valid, then decrypts to get the list back.
        """
        try:
            with open(self.file_path, 'rb') as f:
                data = f.read()  # Read the entire file as bytes.
            if len(data) < 16:
                raise ValueError("Invalid database file: too short")  # Ensure file has at least salt.
            salt = data[:16]
            encrypted_data = data[16:]
            json_data = self.decrypt_data(encrypted_data)  # Decrypt the data.
            return json.loads(json_data)  # Convert JSON back to a Python list.
        except (FileNotFoundError, PermissionError):
            raise ValueError("Cannot access database file.")  # Handle file access issues.
        except InvalidToken:
            raise ValueError("Incorrect password or corrupted data")  # Handle wrong password or bad data.
        except Exception as e:
            raise ValueError(f"Error loading database: {e}")  # Handle any other loading errors.
 
    def add_entry(self, username, password, comment):
        """
        Adds a new username-password pair with a comment and saves the database.
        """
        self.entries.append({"username": username, "password": password, "comment": comment})  # Add new pair with comment to list.
        self.save()  # Save the updated list to the file.
 
    def view_entries(self):
        """
        Shows all stored username-password pairs on the screen, including comments.
        """
        if not self.entries:
            print("No entries found.")  # If list is empty, inform the user.
        else:
            for entry in self.entries:
                print(f"Username: {entry['username']}, Password: {entry['password']}, Comment: {entry['comment']}")  # Print each pair with comment.
 
    def delete_entry(self):
        """
        Deletes an existing entry by user selection.
        """
        if not self.entries:
            print("No entries to delete.")
            return
        print("Current entries:")
        for index, entry in enumerate(self.entries):
            print(f"{index+1}. Username: {entry['username']}, Password: {entry['password']}, Comment: {entry['comment']}")  # Show entries with numbers.
        try:
            index = int(input("Enter the number of the entry to delete: ")) - 1  # Get user choice, adjust for 0-based indexing.
            if 0 <= index < len(self.entries):
                del self.entries[index]  # Remove the selected entry.
                self.save()  # Save the updated database.
                print("Entry deleted and database saved.")
            else:
                print("Invalid entry number.")  # Inform if choice is out of range.
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-numeric input.
 
def main():
    """
    Handles the main program flow, like asking what the user wants to do.
    """
    print("Welcome to the Password Manager")
    while True:
        choice = input("Do you want to (1) create a new database or (2) open an existing one? ")
 
        if choice == '1':
            # Create a new database
            file_path = input("Enter the file path for the new database: ")
            directory = os.path.split(file_path)[0]  # Get the directory part of the path.
            if not os.path.exists(directory):
                print("Directory does not exist. Please enter a valid file path.")  # Check if directory exists.
                continue
            if os.path.exists(file_path):
                confirm = input("File already exists. Do you want to overwrite it? (y/n): ")  # Ask for overwrite confirmation.
                if confirm.lower() != 'y':
                    print("Operation canceled.")
                    continue
            password = getpass("Enter a new encryption password: ")  # Securely get password.
            try:
                db = PasswordDatabase(file_path, password)  # Create new database, salt generated internally.
                print("New database created.")
            except Exception as e:
                print(f"Failed to create database: {e}")  # Show any errors.
                continue
 
        elif choice == '2':
            # Open an existing database
            file_path = input("Enter the file path of the existing database: ")
            if not os.path.exists(file_path):
                print("Database file not found.")  # Check if file exists.
                continue
            try:
                with open(file_path, 'rb') as f:
                    salt = f.read(16)  # Read the first 16 bytes as salt from the file.
                password = getpass("Enter the encryption password: ")  # Securely get password.
                db = PasswordDatabase(file_path, password, salt)  # Open database with existing salt.
                print("Database opened successfully.")
            except ValueError as e:
                print(e)  # Show specific errors like wrong password.
                continue
            except Exception as e:
                print(f"Failed to open database: {e}")  # Show any other errors.
                continue
 
        else:
            print("Invalid choice.")  # If user enters something other than 1 or 2.
            continue
 
        # Main interaction loop, keeps asking until user exits.
        while True:
            action = input("What do you want to do? (1) View entries, (2) Add new entry, (3) Delete entry, (4) Exit: ")
            if action == '1':
                db.view_entries()  # Show all entries.
            elif action == '2':
                username = input("Enter username: ")
                password_entry = input("Enter password: ")  # Get new credentials.
                comment = input("Enter comment (e.g., service name): ")  # Get comment for context, like service.
                db.add_entry(username, password_entry, comment)  # Add and save them.
                print("Entry added and database saved.")
            elif action == '3':
                db.delete_entry()  # Delete an entry.
            elif action == '4':
                print("Exiting.")  # End the program.
                return
            else:
                print("Invalid choice.")  # If user enters something other than 1, 2, 3, or 4.
 
if __name__ == "__main__":
    main()  # Start the program if run directly.
