import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class VigenereCipher:
    @staticmethod
    def encrypt(plaintext, key):
        ciphertext = ""
        key_length = len(key)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift = ord(key[i % key_length].upper()) - ord('A')
                if char.isupper():
                    ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += char
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        plaintext = ""
        key_length = len(key)
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(key[i % key_length].upper()) - ord('A')
                if char.isupper():
                    plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += char
        return plaintext

class VigenereApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Plain text message input
        self.plaintext_input = QLineEdit()
        layout.addWidget(QLabel("Plain Text Message:"))
        layout.addWidget(self.plaintext_input)

        # Encryption key input
        self.key_input = QLineEdit()
        layout.addWidget(QLabel("Encryption Key:"))
        layout.addWidget(self.key_input)

        # Action buttons
        button_layout = QHBoxLayout()
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.setEnabled(False)
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        layout.addLayout(button_layout)

        # Result field
        self.result_field = QTextEdit()
        self.result_field.setReadOnly(True)
        layout.addWidget(QLabel("Result:"))
        layout.addWidget(self.result_field)

        self.setLayout(layout)

        # Connect buttons to functions
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

        self.setWindowTitle('Vigenere Cipher')
        self.setGeometry(300, 300, 400, 300)

    def encrypt(self):
        plaintext = self.plaintext_input.text()
        key = self.key_input.text()
        if plaintext and key:
            ciphertext = VigenereCipher.encrypt(plaintext, key)
            self.result_field.setText(ciphertext)
            self.decrypt_button.setEnabled(True)

    def decrypt(self):
        ciphertext = self.result_field.toPlainText()
        key = self.key_input.text()
        if ciphertext and key:
            plaintext = VigenereCipher.decrypt(ciphertext, key)
            self.result_field.setText(plaintext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VigenereApp()
    ex.show()
    sys.exit(app.exec_())