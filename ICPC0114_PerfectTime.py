from math import sqrt
def prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: return False
    return n >= 2
def Check(n):
    if prime(int(n)) == False:
        return 0
    if prime(int(n[::-1])) == False:
        return 0
    s = 0
    for i in n:
        if(i != '2' and i != '3' and i != '7' and i != '5'): return 0
        s += int(i)
    if prime(s) == False:
        return 0
    return 1
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        if Check(str(n)) == 1:
            print("Yes")
        else:
            print("No")