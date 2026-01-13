import sys, os
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                               QLineEdit, QPushButton, QListWidget, QMessageBox)
from PySide6.QtGui import QIcon
from core.manager import PasswordManager
from core.password_generator import generate_password

class PasswordManagerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setGeometry(300, 200, 500, 400)
        # встановити іконку вікна (шукаємо icon.ico в корені проекту)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_dir, "icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Папки
        os.makedirs("data", exist_ok=True)
        os.makedirs("logs", exist_ok=True)

        self.db_file = "data/passwords.db"
        self.master_password = "1234"  # для тесту, можна замінити на input dialog

        # Ініціалізація менеджера
        if os.path.exists(self.db_file):
            salt = open(self.db_file, "rb").read()[:16]
        else:
            salt = None
        self.manager = PasswordManager(self.db_file, self.master_password, salt)

        # GUI компоненти
        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        layout.addWidget(self.password_input)

        self.comment_input = QLineEdit()
        self.comment_input.setPlaceholderText("Comment")
        layout.addWidget(self.comment_input)

        self.gen_btn = QPushButton("Generate Password")
        self.gen_btn.clicked.connect(self.generate_password)
        layout.addWidget(self.gen_btn)

        self.add_btn = QPushButton("Add Entry")
        self.add_btn.clicked.connect(self.add_entry)
        layout.addWidget(self.add_btn)

        self.entries_list = QListWidget()
        layout.addWidget(self.entries_list)

        self.delete_btn = QPushButton("Delete Selected")
        self.delete_btn.clicked.connect(self.delete_entry)
        layout.addWidget(self.delete_btn)

        self.setLayout(layout)
        self.refresh_entries()

    def generate_password(self):
        pwd = generate_password(12)
        self.password_input.setText(pwd)

    def add_entry(self):
        username = self.username_input.text()
        password = self.password_input.text()
        comment = self.comment_input.text()
        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password cannot be empty")
            return
        self.manager.add(username, password, comment)
        self.refresh_entries()

    def delete_entry(self):
        index = self.entries_list.currentRow()
        if index >= 0:
            self.manager.delete(index)
            self.refresh_entries()

    def refresh_entries(self):
        self.entries_list.clear()
        for entry in self.manager.list_entries():
            self.entries_list.addItem(f"{entry['username']} | {entry['password']} | {entry['comment']}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # глобальна іконка для аплікації (таскбар)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(base_dir, "icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    window = PasswordManagerGUI()
    window.show()
    sys.exit(app.exec())

