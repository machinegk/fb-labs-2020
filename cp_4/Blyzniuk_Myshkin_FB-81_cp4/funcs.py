import math
import random


def gcd(first_number, second_number):
    coefs = []
    # print("gcd of " + str(first_number) + " and " + str(second_number), end=" is ")
    while second_number != 0:
        t = second_number
        if first_number > second_number:
            coefs.append(first_number // second_number)
        second_number = first_number % second_number
        first_number = t
    # print(first_number)
    return first_number, coefs


def find_opposite(a, mod):
    _, coefs = gcd(a, mod)
    # print("coefs: " + str(coefs))
    x = 1
    y = 0
    t = 0
    for index in range(0, (len(coefs) - 1)):
        t = x
        x = x * -(coefs[index]) + y
        y = t
    if x < 0:
        x = x + mod
    # print("opposite is: " + str(x))
    return x


def func_groma(a, power, mod):
    result = 1
    for i in range(0, power):
        result = result * a % mod
    return result


def random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


def random_prime(key_length):
    print("Key length is " + str(key_length))
    lower_bound = 2 ** key_length - 1
    upper_bound = 2 ** (key_length + 1) - 1
    print("Looking for random number in range " + str(lower_bound), str(upper_bound))
    while True:
        print("k", end="")
        rand_number = random_number(lower_bound, upper_bound)
        if rand_number % 2 == 0:
            rand_number += 1
        if miller_rabin_test(rand_number):
            print("We found a prime number: " + str(rand_number))
            break
    print("end of the func")
    return rand_number


def miller_rabin_test(number):
    print("Miller rabin test of number " + str(number))
    k = 100
    s = 0
    d = number - 1
    # number-1 = d * 2^(s) -> d = (number-1) / 2^(s)
    # s - количество двоек в разложении (number - 1)
    while d % 2 == 0:
        s += 1
        d = d // 2  # d = (d - (d % 2)) /2

    for _ in range(0, k):
        # take random x in range 1 < x < number OR 2 <= x <= (number-1)
        x = random_number(2, number - 1)
        if gcd(x, number)[0] > 1:
            # number is not prime
            return False
        else:
            # number can be prime or not
            x =  func_groma(x, d, number) # (x ** d) % number
            if abs(x) == 1:
                # sil`no psevdoprostoe za osnovaniem x
                continue
            for si in range(1, s-1):
                # x_r = x^(d * 2^(si)) -> x^(d) * x^(2^si)
                x_r = (x ** (2 ** si) * x) % number
                if x_r == -1:
                    break
                elif x_r == 1:
                    return False
                else:
                    continue
    return True
