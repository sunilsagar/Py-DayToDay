# a = Complex(1,2)  #re, imag  # __init__
# b = Complex(2,3)  #re, imag 
# c = a+b           # re+re   and imag+imag  # __add__
# print(c)  # Complex( 3,5)  # __str__

class Complex:
    def __init__ (self,u,v):
        self.re = u 
        self.imag = v
    def __add__ (self,other):
        re = self.re + other.re 
        imag = self.imag + other.imag 
        return Complex(re, imag) 
    def __str__(self): 
        return "Complex("+str(self.re)+","+str(self.imag)+")"
if __name__ == '__main__' :
    a=Complex(1,2)
    b=Complex(2,3)
    c=a+b
    print(c)

