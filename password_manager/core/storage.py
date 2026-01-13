import json, os
from cryptography.fernet import InvalidToken
from .crypto import derive_key, encrypt_data, decrypt_data

class PasswordStorage:
    def __init__(self, filepath, password, salt=None):
        self.filepath = filepath
        self.password = password
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if salt is None:
            self.salt = os.urandom(16)
            self.entries = []
            self.key = derive_key(password, self.salt)
            self.save()
        else:
            self.salt = salt
            self.key = derive_key(password, self.salt)
            self.entries = self.load_entries()

    def save(self):
        data = json.dumps(self.entries).encode()
        encrypted = encrypt_data(self.key, data)
        with open(self.filepath, 'wb') as f:
            f.write(self.salt + encrypted)

    def load_entries(self):
        with open(self.filepath, 'rb') as f:
            data = f.read()
        salt = data[:16]
        encrypted = data[16:]
        try:
            decrypted = decrypt_data(self.key, encrypted)
            return json.loads(decrypted)
        except InvalidToken:
            raise ValueError("Incorrect password or corrupted data")

    def add_entry(self, username, password, comment):
        self.entries.append({"username": username, "password": password, "comment": comment})
        self.save()

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self.save()

    def get_entries(self):
        return self.entries
