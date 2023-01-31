a = input()
cnt = 0
for x in a:
    if x == '4' or x == '7':
        cnt += 1
if(cnt == 4 or cnt == 7):
    print("YES")
else :
    print("NO")