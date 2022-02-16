import time

import SieveOfEratosthenes
import SimplePrimeGenerator

n = 1000000

start_time = time.time()
SimplePrimeGenerator.get_primes(n)
end_time_simple = time.time() - start_time

start_time = time.time()
SieveOfEratosthenes.get_primes(n)
end_time_sieve = time.time() - start_time

print("Computation Time")
print("Simple: " + str(end_time_simple))
print("Sieve: " + str(end_time_sieve))
