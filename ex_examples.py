class MyException(Exception):
    pass
def p(x):
    if x < 0 :
            raise MyException("x is negative")
    else:
            return x+2
if __name__ == '__main__':
    correct = False 
    while not correct:
        x = input("Give a number: ")        
        try:
            print(p(int(x)))
            correct = True 
        except MyException as ex:
            print(ex)


