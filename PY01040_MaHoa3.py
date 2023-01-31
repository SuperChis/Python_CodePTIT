def proCess(s):
	cnt = 0
	res = ''
	for i in s:
		cnt += (ord(i) - ord('A'))
	for i in s:
		res += chr((ord(i) - ord('A') + cnt) % 26 + ord('A'))
	return res
for t in range(int(input())):
	s = input()
	a, b = s[:int(len(s)/2)], s[int(len(s)/2):]
	a = proCess(a)
	b = proCess(b)
	ans = ''
	for i in range(len(a)):
		ans += chr((ord(a[i]) + ord(b[i]) - 2*ord('A')) % 26 + ord('A'))
	print(ans)