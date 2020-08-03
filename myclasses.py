class MyInt:
    def __init__(self, v): # a = MyInt(2)
        self.value = v 
    def __add__(self, other): #c = a + b
        z = self.value + other.value 
        return z 
    def __str__(self):      # used by print
        return "MyInt(%d)" % (self.value, )
    def square(self):
        return self.value * self.value
        
        
if __name__ == '__main__':    
    a = MyInt(2)  # self = a
    b = MyInt(3)  # self =b 
    print(a)
    #c = a.add(b)  # self=a, other=b
    c = a + b # a.__add__(b) => self=a, other=b 
    print(c)
    d = b.square() #self = b
    print(d)