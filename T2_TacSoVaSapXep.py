import re

a = list()
for t in range(int(input())):
    s = input()
    a.extend(map(int, re.findall("\d+", s)))
a.sort()
for i in a:
    print(i)
