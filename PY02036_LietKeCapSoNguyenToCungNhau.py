def Gcd(a, b):
    while b != 0:
        a = a % b
        a, b =  b, a
    return a
n = int(input())
a = sorted([int(i) for i in input().split()])
for i in range(n-1):
    for j in range(i+1, n):
        if(Gcd(a[i], a[j]) == 1):
            print(a[i], a[j])
