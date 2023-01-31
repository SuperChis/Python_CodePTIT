import math


def isPrime(n):
    if n < 2: return False
    elif(n > 2):
        if n % 2 == 0: return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True
for t in range(int(input())):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    if(isPrime(s)):
        print("YES")
    else:
        print("NO")