import math


def isPrime(n):
    if n < 2:
        return False
    elif n > 2:
        if n % 2 == 0: return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0: return False
    return True
n = int(input())
a = list(dict.fromkeys([int(i) for i in input().split()]))
l = 0
r = sum(a)
ok = 0
for i in range(len(a)):
    l += a[i]
    r -= a[i]
    if(isPrime(l) and isPrime(r)):
        print(i)
        ok = 1
        break
if ok == 0: print("NOT FOUND")