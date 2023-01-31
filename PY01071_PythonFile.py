s = input().lower()
if s[len(s) - 3:] == '.py' and len(s) >= 3:
    print("yes")
else:
    print("no")
