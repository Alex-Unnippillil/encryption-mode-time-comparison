# -*- coding: utf-8 -*-

import sys, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import padding
import time

def getPlaintext():
    print('File name:')
    try:
        infile = open(input(), 'rb')
        message = infile.read()
        infile.close()
        return message
    except:
        print('An error occured')
        return b'None'

def hamming(a, b):
    return bin(int.from_bytes(a,byteorder=sys.byteorder)^int.from_bytes(b,byteorder=sys.byteorder)).count('1')

padder = padding.PKCS7(128).padder()
backend = default_backend()
k = b'abcdefghijklmnop'
iv = os.urandom(16)
mode = modes.CTR(iv) # edit for mode type #ECB, #CBC, #CFB, #OFB, #CTR, and #XTS-AES
cipher1 = Cipher(algorithms.AES(k), mode, backend=backend)
encryptor1 = cipher1.encryptor()
plaintext = padder.update(getPlaintext())
plaintext += padder.finalize()
t1 = time.time()
ct1 = encryptor1.update(plaintext) + encryptor1.finalize()
t2 = time.time()
print('encryption time using {}: {}'.format(mode.name, t2-t1))

cipher2 = Cipher(algorithms.ARC4(k), mode=None, backend=backend)
encryptor2 = cipher2.encryptor()
t1 = time.time()
ct2 = encryptor2.update(plaintext)
t2=time.time()
print('encryption time using RC4: {}'.format(t2-t1))
