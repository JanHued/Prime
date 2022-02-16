import numpy as np


def is_prime(n):
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def save_primes(n):
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)
    return primes


def get_primes(n):
    return save_primes(n)
