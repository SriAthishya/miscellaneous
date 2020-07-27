class Operation:
  def add(self,a,b):
    """Addition of 2 numbers"""
    c=a+b
    return c
  
  def sub(self,a,b):
    """Subtraction of 2 numbers"""
    c=a-b
    return c
  
  def mul(self,a,b):
    """Multiplication of 2 numbers"""
    c=a*b
    return c
  

obj= Operation()
x=5
y=2
print(obj.add.__doc__)
print(obj.add(x,y))
print(obj.sub.__doc__)
print(obj.sub(x,y))
print(obj.mul.__doc__)
print(obj.mul(x,y))
