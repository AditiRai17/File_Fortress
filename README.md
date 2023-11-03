# File_Fortress
#### Robust and Reliable Defense mechanism for ensuring the confidentiality and integrity of digital information.

The goal of this project is to provide users with a simple yet effective way to protect their files and data from unauthorized access. By employing strong encryption and secure key management, the project aims to give users peace of mind, knowing that their sensitive information is safe, even if their devices are compromised.

## Tech Stack:

  ##### 1. Cryptography Library: The project relies on the cryptography library, specifically using Fernet encryption for securing files.
  ##### 2. Encryption Key Management: The project manages encryption keys securely and stores them in a file named "lockKey.key."
  ##### 3. File System Interaction: utilizes the Python 'os' module for interacting with the file system, enabling it to identify and encrypt files.
  ##### 4. Secure File Handling: The project encrypts files in the current directory while skipping specific files, such as "Encrypt.py," "Decrypt.py," and the "lockKey.key" file.

Let's Understand 

## What is Fernet ?
  - Fernet is Symmetric Encryption method
  - Makes sure the message Encrypted cannot be manipulated/read without the Key.
  - It uses URL safe encoding for the keys . 
  - Fernet also uses 128-bit AES
