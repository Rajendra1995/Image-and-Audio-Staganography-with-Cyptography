from cryptography.fernet import Fernet


def decrypt(encrypted_text, key):
    key = bytes(key, 'utf-8')
    f = Fernet(key)
    return f.decrypt(bytes(encrypted_text, "UTF-8")).decode()
