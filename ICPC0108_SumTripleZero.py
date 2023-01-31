if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort()
        ans = 0
        for i in range(n-1):
            l = i+1
            r = n-1
            while (l < r):
                if(a[i] + a[l] + a[r] == 0):
                    ans += 1
                    l += 1
                elif(a[i] + a[l] + a[r] < 0):
                    l += 1
                else:
                    r -= 1
        print(ans)
