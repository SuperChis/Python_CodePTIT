st = set()
for t in range(int(input())):
    s = input().strip().split()
    res = ''
    for x in s:
        res += x
    st.add(res)
print(len(st))