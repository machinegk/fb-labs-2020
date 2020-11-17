from funcs import *
from rsa import *
import requests

public_key, private_key = generate_key_pair(25)
print()
print("Public key: " + "\n\tPublic exponent: " + str(public_key[0]) + "\n\tModulus: " + str(public_key[1]))
print("Public key(hex): " + "\n\tPublic exponent: " + str(hex(public_key[0])) + "\n\tModulus: " + str(hex(public_key[1])))
print("Public key(site-hex): " + "\n\tPublic exponent: " + str(site_hex(public_key[0])) + "\n\tModulus: " + str(site_hex(public_key[1])))
print()
print("Private key: " + "\n\tSecret: " + str(private_key[0]) + "\n\tModulus: " + str(private_key[1]))
print("Private key(hex): " + "\n\tSecret: " + str(hex(private_key[0])) + "\n\tModulus: " + str(hex(private_key[1])))
print("Private key(site- hex): " + "\n\tSecret: " + str(site_hex(private_key[0])) + "\n\tModulus: " + str(site_hex(private_key[1])))

message = 100
encrypted_message = encrypt(message, public_key)
print()
print("Open message: " + str(message) + "\n\thex: " + str(hex(message)) + "\n\tsite-hex: " + str(site_hex(message)))
print()
print("Encrypted message: " + str(encrypted_message) + "\n\thex: " + str(hex(encrypted_message))+ "\n\tsite-hex: " + str(site_hex(encrypted_message)))
print()

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message: " + str(decrypted_message) + "\n\thex: " + str(hex(decrypted_message)) + "\n\tsite-hex: " + str(site_hex(decrypted_message)))


message, signature = sign(message, private_key)

print()
print("Message signature: " + str(signature) + "\n\thex: " + str(hex(signature)) + "\n\tsite-hex: " + str(site_hex(signature)))
print()

print("Local signature verification: " + str(verify(message, signature, public_key)))

str_request = f"http://asymcryptwebservice.appspot.com/rsa/verify?message={site_hex(message)}&type=BYTES&signature={site_hex(signature)}&modulus={site_hex(public_key[1])}&publicExponent={site_hex(public_key[0])}"
keygen_request = requests.get(str_request)
print("API signature verification: " + str(keygen_request.json()))
print()
print("----------")
print()


key_length = 20

public_key_a, private_key_a = generate_key_pair(key_length)
public_key_b, private_key_b = generate_key_pair(key_length+1)
