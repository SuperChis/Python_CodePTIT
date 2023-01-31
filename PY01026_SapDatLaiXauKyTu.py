t = int(input())
for i in range(t):
    s1 = sorted(input())
    s2 = sorted(input())
    if s1 == s2:
        print("Test {0}: YES".format(i+1))
    else:
        print("Test {0}: NO".format(i+1))



