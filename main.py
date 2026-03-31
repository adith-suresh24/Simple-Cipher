import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ================= BASE64 =================
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

# ================= CAESAR =================
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# ================= AES =================
KEY = b'1234567890123456'  # 16-byte key

def aes_encrypt(text):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def aes_decrypt(enc_text):
    raw = base64.b64decode(enc_text)
    iv = raw[:16]
    ct = raw[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

# ================= MAIN =================
def main():
    print("Choose Algorithm:")
    print("1. Base64")
    print("2. Caesar Cipher")
    print("3. AES")

    choice = input("Enter choice (1-3): ")

    text = input("Enter text: ")

    mode = input("Encode or Decode (e/d): ").lower()

    if choice == '1':
        if mode == 'e':
            print("Encoded:", base64_encode(text))
        else:
            print("Decoded:", base64_decode(text))

    elif choice == '2':
        shift = int(input("Enter shift value: "))
        if mode == 'e':
            print("Encrypted:", caesar_encrypt(text, shift))
        else:
            print("Decrypted:", caesar_decrypt(text, shift))

    elif choice == '3':
        if mode == 'e':
            print("Encrypted:", aes_encrypt(text))
        else:
            print("Decrypted:", aes_decrypt(text))

    else:
        print("Invalid choice!")

main()