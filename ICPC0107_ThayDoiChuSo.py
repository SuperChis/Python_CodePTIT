t = int(input())
while t > 0:
    n, m = [int(i) for i in input().split()]
    try:
        tmp = input().split()
        s1, s2 = [x for x in tmp]
    except:
        s1 = tmp[0]
        s2 = input()
    if n > m:
        t = m
        m = n
        n = t
    print(int(s1.replace(str(m),str(n))) + int(s2.replace(str(m),str(n))), int(s1.replace(str(n),str(m))) + int(s2.replace(str(n),str(m))))
    t -= 1