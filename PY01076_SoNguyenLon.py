t = int(input())
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
while t > 0:
    n = int(input())
    m = int(input())
    print(gcd(n, m,))
    t -= 1