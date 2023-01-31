
def checkS(x):
    sum1 = 0
    while x > 0:
        a = x % 10
        x = int(x / 10)
        sum1 += a
    if(sum1 % 10 == 0):
         return True
    return False

def check2(x):
    while x > 9:
        a =  x % 10
        x = int(x / 10)
        b = x % 10
        if abs(a - b) != 2: 
            return False
    return True
t = int(input())
while t > 0:
    str = int(input())
    if checkS(str) and check2(str):
        print("YES")
    else:
        print("NO") 
    t -= 1