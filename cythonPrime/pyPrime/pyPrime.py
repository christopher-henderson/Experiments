from math import sqrt

def prime(ceiling):
    primes = [2]
    n = 3
    while len(primes) < ceiling:
        mid = sqrt(n)
        prime = True
        for div in primes:
            if div > mid:
                break
            elif n%div is 0:
                prime = False
                break
        if prime:
            primes.append(n)
        n += 2
    return primes[-1]
