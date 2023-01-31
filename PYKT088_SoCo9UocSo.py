def countNumbers(n):
    c = 0
    limit = int(n ** (0.5))

    #Sàng mảng, ban đầu prime[i] = i
    prime = [i for i in range(limit + 1)]

    # su dung sang de luu tru thua so nguyen to dau tien cua moi so
    i = 2
    while i * i <= limit:
        if prime[i] == i:

            # mark all factors of i
            for j in range(i * i, limit + 1, i):
                if prime[j] == j:
                    prime[j] = i

        i += 1

    # kiểm tra tất cả các số nếu chúng có thể được biểu thị dưới dạng p*q
    for i in range(2, limit + 1):

        # p prime factor
        p = prime[i]

        # q prime factor
        q = prime[i // prime[i]]

        # if both prime factors are different
        # if p*q<=n and q!=
        if p * q == i and q != 1 and p != q:
            c += 1

        elif prime[i] == i:

            # Check if it can be
            # expressed as p^8
            if i ** 8 <= n:
                c += 1

    return c

if __name__ == "__main__":
    n = int(input())
    print(countNumbers(n))