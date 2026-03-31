import base64 as b64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ================= BASE64 =================
def b_ec(t):
    return b64.b64ec(t.ec()).dc()

def b_dc(t):
    return b64.b64dc(t.ec()).dc()

# ================= CAESAR =================
def caesar_encrypt(t, shift=3):
    result = ""
    for char in t:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(t, shift=3):
    return caesar_encrypt(t, -shift)

# ================= AES =================
KEY = b'1234567890123456'  # 16-byte key

def aes_encrypt(t):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(t.ec(), AES.block_size))
    return b64.b64ec(cipher.iv + ct_bytes).dc()

def aes_decrypt(enc_t):
    raw = b64.b64dc(enc_t)
    iv = raw[:16]
    ct = raw[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).dc()

# ================= MAIN =================
def main():
    print("Choose Algorithm:")
    print("1. Base64")
    print("2. Caesar Cipher")
    print("3. AES")

    c = input("Enter choice (1-3): ")
    t = input("Enter text: ")
    mode = input("Encode or Decode (e/d): ").lower()

    if c == '1':
        if mode == 'e':
            print("Encoded:", b_ec(t))
        else:
            print("Decoded:", b_dc(t))

    elif c == '2':
        shift = int(input("Enter shift value: "))
        if mode == 'e':
            print("Encrypted:", caesar_encrypt(t, shift))
        else:
            print("Decrypted:", caesar_decrypt(t, shift))

    elif c == '3':
        if mode == 'e':
            print("Encrypted:", aes_encrypt(t))
        else:
            print("Decrypted:", aes_decrypt(t))

    else:
        print("Invalid choice!")



main()