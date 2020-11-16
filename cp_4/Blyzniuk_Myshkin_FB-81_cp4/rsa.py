from funcs import *

def generate_key_pair(key_length):
    # print("Key length is " + str(key_length))
    p = random_prime(key_length)
    q = random_prime(key_length)
    # print("\n owr p = " + str(p) + "\nand q = " + str(q))
    if p == q:
        q = random_prime(key_length)
    n = q * p
    # fi(prime) = (prime - 1)
    fi_n = (q - 1) * (p - 1)
    e = fi_n
    while has_common_divider(e, fi_n):
        e = random_number(2, (fi_n - 1))
    d = find_opposite(e, fi_n)
    public_key = (n, e)
    private_key = (d, p, q)
    return (public_key, private_key)


def encrypt(message, public_key):
    return left_to_right_power(message, public_key[1], public_key[0])


def decrypt():
    pass


def sign():
    pass


def verify():
    pass


def sendKey():
    pass


def receive_key():
    pass
