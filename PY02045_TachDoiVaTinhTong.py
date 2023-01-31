def Head(n):
    return int(n[len(n)//2:])

def End(n):
    return int(n[:int(len(n)/2)])

n = int(input())
while(len(str(n)) > 1):
    n = Head(str(n)) + End(str(n))
    print(n)