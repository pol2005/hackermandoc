#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

fileinput = raw_input("filename: ")
pubinput = raw_input("public key (enter for public_key.pem): ")
if pubinput == "":
	pubinput = "public_key.pem"

#Our Encryption Function
def encrypt_blob(blob, public_key):
    #import keys
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)

    #chunking
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  ""

    while not end_loop:
        #combining chunk
        chunk = blob[offset:offset + chunk_size]

        #check
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))

        #append
        encrypted += rsa_key.encrypt(chunk)

        #increase offset by chunk size
        offset += chunk_size

    #base64 encode
    return base64.b64encode(encrypted)

#use the public key for encryption
fd = open(pubinput, "rb")
public_key = fd.read()
fd.close()

#file to be encrypted
fd = open(fileinput, "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

#write the encrypted contents to a file
fd = open(fileinput, "wb")
fd.write(encrypted_blob)
fd.close()
print("yay! "+fileinput+" has been encrypted using "+pubinput)
