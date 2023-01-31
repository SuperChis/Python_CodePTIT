import re
s = ""
regex = '[\w\s,:]+'
while True:
    try:
        s += input()
    except EOFError:
        break
s = re.findall(regex, s)
for i in s:
    ans = i.lower().split()
    ans[0] = ans[0].title()
    print(ans)
