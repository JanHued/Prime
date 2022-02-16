import numpy as np


def sieve(limit):
    primes = []
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(np.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    for i in range(0, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes


def get_primes(n):
    return sieve(n)
