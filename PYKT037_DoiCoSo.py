alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    n, cs = [int(i) for i in input().split()]
    ans = ''
    while n > 0:
        ans = alpha[n % cs] + ans
        n //= cs
    print(ans)