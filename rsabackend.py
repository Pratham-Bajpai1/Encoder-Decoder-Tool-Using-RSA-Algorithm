import random
import math

def generate_primes():
    primes = []
    while len(primes) < 2:
        candidate = random.randint(100, 1000)
        if is_prime(candidate):
            primes.append(candidate)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keys():
    primes = generate_primes()
    p = primes[0]
    q = primes[1]
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    d = mod_inv(e, phi)
    return (e, n), (d, n)

def encrypt(msg, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in msg]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    msg = [chr((char ** d) % n) for char in cipher]
    return ''.join(msg)
