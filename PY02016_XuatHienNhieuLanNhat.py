
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = dict()
    max = 0
    ans = 0
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > max:
            max = d[i]
    if max > int(n/2):
        for i in d:
            if d[i] == max:
                print(i)
                break
    else:
        print("NO")