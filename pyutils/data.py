#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt

def encrypt_data(plain_txt, key):
	"""Encrypts text or string."""
	encrypted_text = encrypt(key, plain_txt)
	encoded_bytes = b64encode(encrypted_text)
	return encoded_bytes


def decrypt_data(encoded_bytes, key):
	"""Decrypts encrypted text or string."""
	decoded_bytes = bytes(b64decode(encoded_bytes))
	decrypted_text = decrypt(key, decoded_bytes)
	formatted_bytes = str(decrypted_text)
	formatted_text = formatted_bytes[2:(len(formatted_bytes) - 1)]
	return formatted_text
