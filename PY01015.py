
def check(x):
    for i in range(len(x) - 1):
        if x[i] > x[i+1]: 
            return False
    return True
t = int(input())
while t > 0:
    str = input()
    if check(str) ==  True:
        print("YES")
    else:
        print("NO")
    t -= 1
