str = input()
cnt = 0
for x in range(len(str)):
    if(str[x] >= 'A' and str[x] <= 'Z'):
        cnt += 1
    else:
        cnt -= 1
if cnt > 0:
    print(str.upper())
else:
    print(str.lower())
