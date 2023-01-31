def sieve(n, prime):
    p = 2 #first prime number
    while(p * p <= n):
        if(prime[p] == True):
            i = p*2 #start with multiple
            while(i <= n):
                prime[i] = False
                i += p #
        p += 1
def init(n):
    prime = [True] * (n+1)
    sieve(n, prime)
    cnt = 0
    for i in range(2, n-6+1):
        if(prime[i] == True and prime[i+2] == True and prime[i+6] == True): cnt += 1
        elif(prime[i] == True and prime[i+4] == True and prime[i+6] == True): cnt += 1
    print(cnt)
if __name__ == '__main__':
    for t in range(int(input())):
         n = int(input())
         init(n)