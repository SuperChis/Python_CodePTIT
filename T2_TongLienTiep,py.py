def countConsecutive(N):
    count = 0
    L = 1
    while(L * (L + 1) < 2 * N):
        a = (1.0 * N - (L * (L + 1)) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return count
for i in range(int(input())):
    print(countConsecutive(int(input())))

# N = a + (a+1) + (a+2) + .. + (a+L)
# => N = (L+1 )*a + (L*(L+1))/2
# => a = (N- L*(L+1)/2)/(L+1)