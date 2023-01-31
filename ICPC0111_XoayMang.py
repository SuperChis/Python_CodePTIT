for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    print(*a[m:], *a[:m])