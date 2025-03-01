import oqs
import os
from pprint import pformat
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate key pair
kemalg = "ML-KEM-512"
with oqs.KeyEncapsulation(kemalg) as client:
    with oqs.KeyEncapsulation(kemalg) as server:
        print(f"Key encapsulation details:\n{pformat(client.details)}")

        # Client generates its keypair
        public_key_client = client.generate_keypair()

        # Simulate key exchange (normally, this is done between two parties)
        encapsulated_key, shared_secret = server.encap_secret(public_key_client)

        # Derive an AES-256 key from the shared secret
        aes_key = shared_secret[:32]  # Use first 32 bytes for AES-256

# AES-GCM encryption
def encrypt_file(input_file, output_file, key):
    iv = os.urandom(12)  # Generate a random IV
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    with open(input_file, "rb") as f:
        plaintext = f.read()
    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    
    with open(output_file, "wb") as f:
        f.write(iv + encryptor.tag + ciphertext)  # Store IV, tag, and ciphertext

# AES-GCM decryption
def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    
    iv = data[:12]  # First 12 bytes: IV
    tag = data[12:28]  # Next 16 bytes: GCM tag
    ciphertext = data[28:]  # Remaining: Encrypted content

    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file, "wb") as f:
        f.write(plaintext)

# Encrypt a file
encrypt_file("plain.txt", "encrypted.bin", aes_key)

# Decrypt the file
decrypt_file("encrypted.bin", "decrypted.txt", aes_key)

print("Decryption complete. Check 'decrypted.txt'.")