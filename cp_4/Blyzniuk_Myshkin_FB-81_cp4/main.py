from funcs import *
from rsa import *

public_key, private_key = generate_key_pair(1024)
print("Public: " + str(public_key))
print("Public(hex): " + str(key_hex(public_key)))
print("Public(site-hex): " + str(site_key_hex(public_key)))
print()
print("Private: " + str(private_key))
print("Private: " + str(key_hex(private_key)))

message = random_number(1, 1000000)
encrypted_message = encrypt(message, public_key)
print()
print("Open message: " + str(message) + " hex: " + str(hex(message)) + " site-hex: " + str(site_hex(message)))
print()
print("Encrypted message: " + str(encrypted_message))
print("Encrypted message(hex): " + str(hex(encrypted_message)))
print("Encrypted message(site-hex): " + str(site_hex(encrypted_message)))
