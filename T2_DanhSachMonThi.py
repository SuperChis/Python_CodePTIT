
class MonThi:

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def getid(self):
        return self.id

    def __str__(self):
        return f"{self.id} {self.name} {self.type}"

if __name__ == '__main__':
    a = list()
    for t in range(int(input())):
        m = MonThi(input(), input(), input())
        a.append(m)
    a.sort(key= lambda x: x.id)
    for i in a:
        print(i)