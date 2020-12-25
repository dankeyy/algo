#!/usr/bin/env python3

def get_primes(n):
    candidates = set(range(2, n + 1)) # 2 sets are needed because we can't both iterate over a set and subtract values from it at the same time.
    primes = set(range(2, n + 1))

    for i in candidates: # subtracting all multiplies of i every iteration
        if i in primes:
            primes -= set(range(2 * i, n + 1, i)) 
    
    return primes
if __name__ == '__main__':
    print( get_primes( int( input('I want prime numbers up to: ') ) ) )
