# 🔐 Python Encryption Toolkit

A simple Python-based encryption and encoding toolkit that demonstrates three commonly used techniques:

- **Base64 Encoding/Decoding**
- **Caesar Cipher Encryption/Decryption**
- **AES-128 Encryption/Decryption (CBC Mode)**

This project is intended for educational purposes to help understand the basics of data encoding and cryptography.

---

# Features

- ✅ Base64 Encode and Decode
- ✅ Caesar Cipher Encrypt and Decrypt
- ✅ AES-128 Encryption (CBC Mode)
- ✅ AES Decryption
- ✅ Interactive Command-Line Interface (CLI)
- ✅ Simple and Beginner-Friendly Code

---

# Algorithms Used

## 1. Base64

Base64 is an encoding scheme, **not encryption**.

It converts binary data into readable ASCII characters.

Example:

```
Hello
```

becomes

```
SGVsbG8=
```

---

## 2. Caesar Cipher

A classical substitution cipher where every alphabet is shifted by a fixed number.

Example (Shift = 3)

```
HELLO
```

becomes

```
KHOOR
```

Decryption shifts characters in the opposite direction.

---

## 3. AES (Advanced Encryption Standard)

This project uses:

- AES-128
- CBC (Cipher Block Chaining) Mode
- PKCS7 Padding
- Random Initialization Vector (IV)

The IV is automatically generated and stored together with the ciphertext.

The encrypted output is Base64 encoded for easier storage and transmission.

---

# Project Structure

```
Python-Encryption-Toolkit/
│
├── encryption_tool.py
├── README.md
└── requirements.txt
```

---

# Requirements

Python 3.8+

Required package:

```
pycryptodome
```

Install using:

```bash
pip install pycryptodome
```

or

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```
pycryptodome
```

---

# How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/Python-Encryption-Toolkit.git
```

Go into the project

```bash
cd Python-Encryption-Toolkit
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python encryption_tool.py
```

---

# Program Menu

```
Choose Algorithm:

1. Base64
2. Caesar Cipher
3. AES

Enter choice (1-3):
```

Then enter:

- Text
- Encode/Decode
- Shift value (for Caesar)

---

# Example

## Base64

Input

```
Choice: 1
Text: Hello World
Mode: e
```

Output

```
Encoded:
SGVsbG8gV29ybGQ=
```

---

## Caesar Cipher

Input

```
Choice: 2
Shift: 5
Text: HELLO
Mode: e
```

Output

```
MJQQT
```

Decryption

```
HELLO
```

---

## AES

Input

```
Choice: 3
Text: Secret Message
Mode: e
```

Output

```
+5b7Mg6m6...
```

Decrypting the encrypted string returns

```
Secret Message
```

---

# How AES Works in this Project

1. User enters plaintext.
2. Data is padded.
3. A random IV is generated.
4. AES encrypts the data.
5. IV + Ciphertext are combined.
6. Result is Base64 encoded.

During decryption:

1. Base64 is decoded.
2. IV is extracted.
3. Ciphertext is decrypted.
4. Padding is removed.
5. Original message is returned.

---

# Libraries Used

| Library | Purpose |
|----------|---------|
| base64 | Encoding and decoding |
| pycryptodome | AES cryptography |
| Crypto.Cipher.AES | AES implementation |
| Crypto.Util.Padding | Data padding |

---

# Security Notes

### Base64

- Not encryption
- Easily reversible
- Used only for encoding

### Caesar Cipher

- Very weak
- Easily brute-forced
- Educational purposes only

### AES

- Strong symmetric encryption
- Uses CBC mode
- Random IV for every encryption
- Suitable for learning modern cryptography

---

# Limitations

- AES key is hardcoded.
- No password-based key generation.
- No file encryption support.
- Command-line interface only.
- No authentication (HMAC/GCM).

---

# Future Improvements

- Add DES encryption
- Add Triple DES
- Add RSA public-key encryption
- Add Fernet encryption
- Password-derived AES keys (PBKDF2)
- File encryption/decryption
- Drag-and-drop file support
- GUI using Tkinter or PyQt
- Export encrypted files
- Secure key management
- Support AES-192 and AES-256
- Add logging
- Improve error handling

---

# Learning Objectives

This project helps understand:

- Data Encoding
- Symmetric Encryption
- Classical Cryptography
- Initialization Vectors (IV)
- Padding
- AES CBC Mode
- Python Cryptography Libraries

---

# License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it for educational and personal purposes.

---

# Disclaimer

This project is designed for **educational purposes only**.

While AES is a secure encryption algorithm, this implementation uses a hardcoded key and is **not intended for production or real-world security applications**. For production systems, implement secure key management, authentication, and best security practices.

---

# Author
Is ME
**Adith**

Python Cryptography Learning Project
