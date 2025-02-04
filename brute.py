#Import required modules
import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from signal import signal,SIGINT

def handler(signal_received, frame):
    print("exiting program")
    print(f'Keys Tried {keysTried}')
    print(f'Final key {key}')
    print(f'Target plaintext {target}')
    print(f'Final plaintext {pt}')
    exit(0)

print("starting program")
signal(SIGINT, handler)
#Define variables necessary for operation
keysTried = 1
key = b'1234567890abcdef'
iv = b'zxcvbnmlkjhgfdsa'

#cryptography.hazmat.backends.default_backend()
data = sys.stdin.buffer.read()
target = b'LoveCryptography'
cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
decryptor = cipher.decryptor()
pt = decryptor.update(data) + decryptor.finalize()
if(target == pt):
    handler(0,0)
while not(target == pt):
    keysTried += 1
    key = (int.from_bytes(key, byteorder='big') + 1).to_bytes(16,'big')
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(data) + decryptor.finalize()
handler(0,0)