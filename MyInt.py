class MyInt:
    def __init__(self,v): #1, a = MyInt(2) => MyInt.__init__(a,2)
        self.value = v 
    def __add__(self, other): #2, a.add(b), self=a other=b
        z = self.value + other.value
        tmp = MyInt(z)
        return tmp
    def __str__(self): #3, print(a)
        return "MyInt("+str(self.value)+")"
    def __eq__(self, other): #2, a.add(b), self=a other=b
        z = self.value == other.value
        return z  
    def square(self):
        return MyInt(self.value ** 2)
        
        
if __name__ == '__main__':
    a = MyInt(2)
    b = MyInt(3)
    c = a + b            # __add__
    print(c)
    print(a == MyInt(2)) # __eq__
    d = a.square()
    print(d)