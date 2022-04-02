from cryptography.fernet import Fernet
# Put this somewhere safe!


def encrypt(plain_text):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_text = f.encrypt(bytes(plain_text, "UTF-8"))
    return encrypted_text.decode(), key

