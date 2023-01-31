t = int(input())
while t > 0:
    str = input()
    ans = "YES"
    for x in range(len(str)):
        if(str[x] != '4' and str[x] != '7'):
            ans = "NO"
            break
    print(ans)
    t -= 1
    