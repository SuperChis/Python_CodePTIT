import re

for t in range(int(input())):
    n = input()
    a = list()
    a.extend(map(int, re.findall('\d+', n)))
    print(min(a))

