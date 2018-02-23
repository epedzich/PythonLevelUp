import math


def is_prime(cur, primes):
    sqrt = math.sqrt(cur)
    for prime in primes:
        if prime > sqrt:
            return True
        if cur % prime == 0:
            return False
    return True


def historic(n):
    primes = [2]
    cur = 3
    while True:
        if is_prime(cur, primes):
            primes.append(cur)
            if len(primes) == n:
                return primes
        cur += 1


found = historic(1234567)
print(found)
print(sum(found))
