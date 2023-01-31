t = int(input())
while t > 0:
    p1 = int(input())
    q1 = int(input())
    p = str(p1)
    q = str(q1)
    a = input()
    b = input()
    amax = amin = a
    bmax = bmin = b
    if p < q:
        amax.replace('p', 'q')
        bmax.replace('p', 'q')
        amin.replace('q', 'p')
        bmin.replace('q', 'p')
        ans1 = int(amin) + int(bmin)
        ans2 = int(amax) + int(bmax)
        print(ans1, ans2)
    else:
        amin.replace('p', 'q')
        bmin.replace('p', 'q')
        amax.replace('q', 'p')
        bmax.replace('q', 'p')
        ans1 = int(amin) + int(bmin)
        ans2 = int(amax) + int(bmax)
        print(ans1, ans2)
    t -= 1

