def Check(n):
    if len(n) < 2: return False
    if n != n[::-1]: return False
    return True
for t in range(int(input())):
    n = int(input())
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if Check(str(s)): print("YES")
    else: print("NO")