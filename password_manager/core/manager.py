from .storage import PasswordStorage

class PasswordManager:
    def __init__(self, filepath, password, salt=None):
        self.storage = PasswordStorage(filepath, password, salt)

    def add(self, username, password, comment):
        self.storage.add_entry(username, password, comment)

    def delete(self, index):
        self.storage.delete_entry(index)

    def list_entries(self):
        return self.storage.get_entries()
