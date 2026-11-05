from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as loaded_key:
        return loaded_key.read()