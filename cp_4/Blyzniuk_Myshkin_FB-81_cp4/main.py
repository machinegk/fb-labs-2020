from funcs import *
from rsa import *

public_key, private_key = generate_key_pair(256)
print()
print("Public key: " + "\n\tPublic exponent: " + str(public_key[0]) + "\n\tModulus: " + str(public_key[1]))
print("Public key(hex): " + "\n\tPublic exponent: " + str(hex(public_key[0])) + "\n\tModulus: " + str(hex(public_key[1])))
print("Public key(site-hex): " + "\n\tPublic exponent: " + str(site_hex(public_key[0])) + "\n\tModulus: " + str(site_hex(public_key[1])))
print()
print("Private key: " + "\n\td: " + str(private_key[0]) + "\n\tp: " + str(private_key[1]) + "\n\tq: " + str(private_key[2]))
print("Private key(hex): " + "\n\td: " + str(hex(private_key[0])) + "\n\tp: " + str(hex(private_key[1])) + "\n\tq: " + str(hex(private_key[2])))
print("Private key(site- hex): " + "\n\td: " + str(site_hex(private_key[0])) + "\n\tp: " + str(site_hex(private_key[1])) + "\n\tq: " + str(site_hex(private_key[2])))

message = 100
encrypted_message = encrypt(message, public_key)
print()
print("Open message: " + str(message) + "\n\thex: " + str(hex(message)) + "\n\tsite-hex: " + str(site_hex(message)))
print()
print("Encrypted message: " + str(encrypted_message) + "\n\thex: " + str(hex(encrypted_message))+ "\n\tsite-hex: " + str(site_hex(encrypted_message)))
print()

decrypted_message = decrypt(encrypted_message, private_key[0], public_key[1])
print("Decrypted message: " + str(decrypted_message) + "\n\thex: " + str(hex(decrypted_message)) + "\n\tsite-hex: " + str(site_hex(decrypted_message)))


message, signature = sign(message, private_key[0], public_key[1])

print()
print("Message signature: " + str(signature) + "\n\thex: " + str(hex(signature)) + "\n\tsite-hex: " + str(site_hex(signature)))
print()

print("Valid signature: " + str(verify(message, signature, public_key)))
print()

