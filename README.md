**WARNING: MALWARE EXAMPLE – FOR EDUCATIONAL USE ONLY**
This script demonstrates how a basic ransomware/malware encryption tool works. DO NOT USE THIS CODE MALICIOUSLY. Unauthorized file encryption on systems you do not own is illegal and unethical. This repository is for cybersecurity education only to help understand attack methods and improve defenses.

**Description**
This Python script simulates a ransomware-like file encryption/decryption tool using the Fernet symmetric encryption scheme from the cryptography library.
The tool:
- Encrypts all files in a directory (excluding itself)
- Requires a secret passphrase for decryption
- Demonstrates how attackers lock files and demand a key for recovery

**How It Works**

*Encryption Process (Malware Simulation)*
- Scans the current directory for files to encrypt
- Excludes itself (encrypt.py, decrypt.py, thekey.key)
- Generates a strong encryption key and saves it in thekey.key
- Encrypts each file, appends .enc extension
- Deletes the original files (simulating ransomware behavior)

*Decryption Process (Recovery Simulation)*
- Requires the correct secret phrase ("coffee" by default)
- Searches for .enc files
- Uses the stored key to decrypt files
- Restores original filenames (removes .enc)
- Deletes encrypted versions after decryption

**Legal & Ethical Disclaimer**
- This is malware-like code for educational purposes only.
- Do not use this on any system without explicit permission.
- Unauthorized encryption of files (ransomware) is a serious crime in most jurisdictions.
- Meant for ethical hacking, cybersecurity training, and research.
- The creator is not responsible for any misuse of this code.

**Requirements**
- Python 3.x
- Cryptography library (pip install cryptography)

**Usage**
- Study the code to understand how file encryption malware works.
- Run in a controlled environment (VM, sandbox) for analysis.
- Modify for defensive research, such as building detection mechanisms.

**Security Notes**
- The default passphrase is "coffee" (change in code if testing).
- The thekey.key file is crucial for decryption (simulates attacker-held key).
- Real ransomware would use stronger encryption, network communication, and persistence mechanisms.
