for i in range(int(input())) :
    s = input()
    k = 1
    for i in range(1, len(s)) :
        if s[i] != s[i - 1] :
            print(k, end = "")
            print(s[i - 1], end = "")
            k = 1
        else : k += 1
    print(k, end = "")
    print(s[len(s) - 1])