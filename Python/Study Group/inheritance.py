class Child():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print(self):
        print(self.a,self.b)

'''class Child1():
    def __init__(self,b):
        self.b=5;
    def print1(self):
        print(self.b)'''

class Parent(Child):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def add(self):
        self.c=self.a+self.b
        print(self.c)

obj=Parent(4,5,0)
obj.add()