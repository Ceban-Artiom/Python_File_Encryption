import os
from cryptography.fernet import Fernet

# Load the key
with open("thekey.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)
files_to_decrypt = []

# Collect encrypted files
for file in os.listdir():
    if file.endswith(".enc") and os.path.isfile(file):
        files_to_decrypt.append(file)

# Secret phrase and User phrase
secretphrase = "coffee"
userphrase = input("Enter the secret phrase: ")

# Decrypt and restore original files
if userphrase == secretphrase:
        for file in files_to_decrypt:
                original_name = file[:-4]  # Remove ".enc"
                with open(file, "rb") as f:
                        encrypted = f.read()
                try:
                        decrypted = fernet.decrypt(encrypted)
                except Exception as e:
                        print(f"Error decrypting {file}: {e}")
                        continue
                with open(original_name, "wb") as f:
                        f.write(decrypted)
                os.remove(file)  # Delete encrypted file
        print(f"{len(files_to_decrypt)} files have been decrypted.")
else:
        print("Wrong secret phrase. Decryption unsuccessful.")