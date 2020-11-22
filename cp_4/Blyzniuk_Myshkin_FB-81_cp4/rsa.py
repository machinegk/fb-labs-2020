from funcs import *


def generate_key_pair(key_length):
    # print("Key length is " + str(key_length))
    p = random_prime(key_length)
    q = random_prime(key_length)
    while p == q:
        q = random_prime(key_length)
    # print("\nowr p = " + str(p) + "\nand q = " + str(q))
    n = q * p
    # fi(prime) = (prime - 1)
    fi_n = (q - 1) * (p - 1)
    e = random_number(2, (fi_n - 1))

    while has_common_divider(e, fi_n):
        e = random_number(2, (fi_n - 1))

    d = find_opposite(e, fi_n)
    public_key = [e, n]
    private_key = [d, n]  # [d, p, q]
    return [public_key, private_key]


def encrypt(message, public_key):
    return left_to_right_power(message, public_key[0], public_key[1])


def decrypt(enc_message, private_key):
    return left_to_right_power(enc_message, private_key[0], private_key[1])


def sign(original_message, private_key):
    signature = left_to_right_power(original_message, private_key[0], private_key[1])
    return [original_message, signature]


def verify(message, signature, public_key):
    success = (message == left_to_right_power(signature, public_key[0], public_key[1]))
    return success


def send_key(a_message, a_private, b_public):
    s = sign(a_message, a_private)
    print(f"User A put \n\tk: {s[0]}\n\ts: {s[1]}\n")
    k1 = left_to_right_power(s[0], b_public[0], b_public[1])
    s1 = left_to_right_power(s[1], b_public[0], b_public[1])
    return (k1, s1)


def receive_key(povidomlennia, public_key_a, public_key_b, private_key_b):
    k1, s1 = povidomlennia
    k = left_to_right_power(k1, private_key_b[0], public_key_b[1])
    s = left_to_right_power(s1, private_key_b[0], public_key_b[1])
    print(f"User B finds \n\tk: {k}\n\ts: {s}\n")
    return k == left_to_right_power(s, public_key_a[0], public_key_a[1])
