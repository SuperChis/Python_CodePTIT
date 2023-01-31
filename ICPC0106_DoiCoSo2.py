import math
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    cs = int(input())
    n = input()
    if(cs == 2):
        print(n)
    else:
        base = int(math.log2(int(n)))
        res = ''
        while len(n) % base != 0: n = '0' + n
        for i in range(len(n)-1,-1,-1):
            cnt = 1
            tmp = 0
            while cnt < base:
                if n[i] == '1':
                    tmp += 2**cnt
                    cnt += 1
                else:
                    cnt += 1
            res = alpha[tmp] + res
        print(res)