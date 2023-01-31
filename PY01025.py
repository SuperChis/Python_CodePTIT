s = input()
i = len(s) - 1 # i = 8
cnt = 0
res = ""
while 1:
    res = s[i] + res
    cnt += 1
    if i == 0: 
        break
    if cnt == 3:
        res = ',' + res 
        cnt = 0
    i -= 1
print(res)