from math import sqrt
def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

def sieve(prime, n):
    for p in range(2, int(sqrt(n))):
        if prime[p] == True:
            for i in range(p*2, n+1, p):
                prime[i] = False

for t in range(int(input())):
    n = int(input())
    prime = [True] * (n + 1)
    prime[1] = False
    sieve(prime, n)
    for i in range(10, n+1):
        if reverse_number(i) < n:
            if prime[i] and prime[reverse_number(i)] and i != reverse_number(i):
                prime[reverse_number(i)] = False
                print(i, reverse_number(i), end = " ")
    print()