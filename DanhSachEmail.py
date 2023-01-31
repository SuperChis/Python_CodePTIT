file = open('Contact.txt', 'r')
list = {i.lower().strip() for i in file}
print(*sorted(list, key=lambda e: e), sep='\n')

