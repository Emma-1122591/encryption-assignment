import os
from cryptography.fernet import Fernet

def key_generator():
    key = Fernet.generate_key()
    with open("../secret.key", "wb") as key_file:
        key_file.write(key)

os.chmod("../secret.key", 0o600)
key_generator()