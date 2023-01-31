str1 = input()
str2= input()
a = int(input())
ans = str1[:a] + str2 + str1[a:]
print(ans)