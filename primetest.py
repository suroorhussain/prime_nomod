from sys import argv

script, limit = argv

def primes(n) :
    num = range(2, n+1)
    primes = []
    while len(num) != 0  :
        temp = num[0]
        primes.append(temp)
        sieve = [temp]
        j = 0
        while n > sieve[-1] :
            sieve.append(temp * num[j])
            j += 1
        num = [x for x in num if x not in sieve]
    print primes

primes(int(limit))
