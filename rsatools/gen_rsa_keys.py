#!/usr/bin/env python3

def generate_RSA(bits=4096):
    from Crypto.PublicKey import RSA
    import random
    print("generating 4096 bit rsa priv&pub key..")
    new_key = RSA.generate(bits)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    private_key = private_key.decode()
    public_key = public_key.decode()
    pubkey = open("public_key.pem","w")
    pubkey.truncate(0)
    pubkey.write(public_key)
    print("public_key.pem    written")
    privkey = open("private_key.pem","w")
    privkey.truncate(0)
    privkey.write(private_key)
    print("private_key.pem written")
    privkey.close()
    pubkey.close()
    print("done")

    return private_key, public_key

generate_RSA();
