def factorial(f):
    for i in range(2, 10):
        f[i] = f[i-1] * i
def Check(n):
    s = 0
    for i in n:
        s += f[int(i)]
    return s == int(n)
for t in range(int(input())):
    n = input()
    f = [1] * 10
    factorial(f)
    if Check(n):
        print("Yes")
    else:
        print("No")