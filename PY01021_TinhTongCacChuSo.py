t = int(input())
while(t > 0):
    s = input()
    Sum = 0
    ans = ""
    for i in range(len(s)):
        if(s[i].isalpha()):
            ans += s[i]
        else:
           Sum += int(s[i])
    print(''.join(sorted(ans)) + str(Sum))
    t -= 1
