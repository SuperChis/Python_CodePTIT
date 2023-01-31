def console(s):
    cnt = 0
    while(len(s) > 1):
        Sum = 0
        for i in s:
           Sum += ord(i) - ord('0')
        cnt += 1
        s = str(Sum)
    print(cnt)
if __name__ == '__main__':
    s = input()
    console(s)
