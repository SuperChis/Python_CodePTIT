t = int(input())
while t > 0:
    str = input()
    if str[0] == str[len(str) - 2] and str[1] == str[len(str) - 1]:
        print("YES")
    else:
        print("NO")
    t -= 1