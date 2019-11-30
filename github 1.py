class MyException(Exception):
    def __init__(self,v):
        self.v= v
    def   str  (self):
        return str(self.v)

def xyz(a,b) :
    c=a+b
    if c>150:
        raise MyException('Custom Exception Occurred')
    else:
        return c

v= xyz(24,34)
print(v)