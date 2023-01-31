a = [0] * 100
a[1] = 1
a[2] = 1
for i in range(3, 95):
    a[i] = a[i-1] + a[i-2]
if __name__ == '__main__':
    for t in range(int(input())):
        n, m = [int(i) for i in input().split()]
        for i in range(n,m +1):
            print(a[i], end = " ")
        print()