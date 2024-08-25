# Vigenere Cipher GUI Application

This is a Python application that implements a graphical user interface for the Vigenere cipher using PyQt5. The Vigenere cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages.

## Features

- **User-friendly GUI**: The application provides a simple and intuitive graphical interface for users to interact with the Vigenere cipher.

- **Text Encryption**: Users can enter a plaintext message and an encryption key to encrypt the message using the Vigenere cipher algorithm.

- **Text Decryption**: The application allows users to decrypt previously encrypted messages using the same key that was used for encryption.

- **Real-time Results**: The encrypted or decrypted text is displayed immediately in the result field after the respective operation.

- **Input Validation**: The 'Decrypt' button is disabled until a message has been encrypted, preventing unnecessary errors.

- **Preserves Non-alphabetic Characters**: The cipher implementation maintains spaces, punctuation, and other non-alphabetic characters in their original positions.

## Capabilities

1. **Message Input**: Users can enter the text to be encrypted in a dedicated input field.

2. **Key Input**: A separate input field is provided for entering the encryption/decryption key.

3. **Encrypt Functionality**: Users can encrypt their message by clicking the 'Encrypt' button.

4. **Decrypt Functionality**: After encryption, users can decrypt the message by clicking the 'Decrypt' button.

5. **Result Display**: The application displays the result (encrypted or decrypted text) in a read-only text area.

6. **Interactive UI Elements**: The 'Decrypt' button is initially disabled and becomes enabled only after a message has been encrypted.

7. **Persistent Key**: The encryption key remains in the input field, allowing for easy decryption without re-entering the key.

## Technical Details

- **Language**: Python 3.x
- **GUI Framework**: PyQt5
- **Cipher Algorithm**: Vigenere Cipher

This application serves as both a practical tool for simple text encryption and a demonstrative project for PyQt5 GUI development and classical cryptography implementation in Python.
