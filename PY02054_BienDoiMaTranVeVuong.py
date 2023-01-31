n, m = [int(i) for i in input().split()]
if n > m:
    for i in range(0, n):
        if(i % 2 == 0 and n > m):
            a = [int(i) for i in input().split()]
            m += 1
            continue
        else:
            print(*[int(i) for i in input().split()])
# elif n < m:
#     for i in range(0, m):
#         if (i % 2 != 0 and n > m):
#             m += 1
#             continue
#         else:
#             print([int(i) for i in input().split()])