n = int(input())
a = [int(i) for i in input().split()]
check = 0
for i in range(1, len(a)):
    if(a[i] - a[i-1] != 1):
        check = 1
        print(a[i]-1)
if(not check):
    print(a[len(a)-1] + 1)