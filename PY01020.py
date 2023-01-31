t = int(input())
while t > 0:
    a = input()
    if a[len(a) - 2] == '8' and a[len(a) - 1] == '6':
        print("YES")
    else: 
        print("NO")
    t -= 1