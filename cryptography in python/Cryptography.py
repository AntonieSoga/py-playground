# Symetric Encryption - AES

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

nonce = os.urandom(12)

data = b"sensitive data"

ciphertext = aesgcm.encrypt(nonce,data,None)
print(ciphertext)

plaintext = aesgcm.decrypt(nonce,ciphertext,None)
print(plaintext)


# Asymetric Encryption - RSA
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"Secret Message"

encrypted = public_key.encrypt(message,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(encrypted)

decrypted = private_key.decrypt(encrypted,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(decrypted)
