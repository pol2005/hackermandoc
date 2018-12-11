#!/usr/bin/env python
#ch9_decrypt_blob.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib

decryptfile = raw_input("file to decrypt: ")
decryptfileoutput = raw_input("new file name: ")
privinput = raw_input("private key (enter for private_key.pem): ")
if privinput == "":
	privinput = "private_key.pem"

#decryption function
def decrypt_blob(encrypted_blob, private_key):

    #import rsa key
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    #base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    #chunk settings
    chunk_size = 512
    offset = 0
    decrypted = ""

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    return zlib.decompress(decrypted)

#Use the private key for decryption
fd = open(privinput, "rb")
private_key = fd.read()
fd.close()

#Our candidate file to be decrypted
fd = open(decryptfile, "rb")
encrypted_blob = fd.read()
fd.close()

#Write the decrypted contents to a file
fd = open(decryptfileoutput, "wb")
fd.write(decrypt_blob(encrypted_blob, private_key))
fd.close()

print("yay! " + decryptfile + " has been decrypted using: "+privinput+" and was saved to: "+decryptfileoutput )
