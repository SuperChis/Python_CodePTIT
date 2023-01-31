
class Student:

    def __init__(self, id, name, gr):
        self.id = id
        self.name = name
        self.gr = gr
        self.Dk = ''

    def getId(self):
        return self.id
    def setCc(self, cc):
        self.Cc = cc
    def setDk(self):
        self.Dk = 'KDDK'
    def getDk(self):
        return self.Dk
    def __str__(self):
        if self.getDk() != '':
            return f'{self.id} {self.name} {self.gr} {self.Cc} {self.getDk()}'
        else:
            return f'{self.id} {self.name} {self.gr} {self.Cc}'

if __name__ == '__main__':
    a = list()
    t = int(input())
    for _ in range(t):
        id = input()
        name = input()
        gr = input()
        x = Student(id, name, gr)
        a.append(x)
    for _ in range(t):
        id, s = [i for i in input().split()]
        cc = 10
        for i in s:
            if(i == 'm'):
                cc -= 1
            if(i == 'v'):
                cc -= 2
        for i in a:
            if i.getId() == id:
                if cc <= 0:
                    i.setCc(0)
                    i.setDk()
                else:
                    i.setCc(cc)
                break
    for i in a:
        print(i)