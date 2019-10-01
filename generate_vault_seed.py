#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from base64 import b64encode

def generate_seed():
    # Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    # The private key in PEM format
    private_key = new_key.exportKey("PEM")

    # base64 encode
    seed = b64encode((private_key))

    print(seed)


if __name__ == '__main__':
    generate_seed()