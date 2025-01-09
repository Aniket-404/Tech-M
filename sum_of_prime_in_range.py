# sum of smallest and largest prime number

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def sum_prime(start,end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)

    if primes:
        return primes[0] + primes[-1]
    return 0

start, end = 1, 5
print(sum_prime(start,end))
