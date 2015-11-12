from sys import argv

script, limit = argv

def primes(n) :
    num = range(2, n+1)
    primes = []
    # for i in range(2,n+1) :
    #     num.append(i)
    print num
    while len(num) != 0  :
        temp = num[0]
        primes.append(temp)
        sieve = [temp]
        j = 0
        while n > sieve[-1] :
            # print "before", j
            sieve.append(temp * num[j])
            # print sieve
            # print sieve[-1]
            j += 1
            # print "after", j
            # print "sieve", sieve
        num = [x for x in num if x not in sieve]
        # print "temp list", temp_list
        # num = temp_list
        print "prime", primes
        print "num", num

primes(int(limit))
