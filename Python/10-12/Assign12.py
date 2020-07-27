class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def getX(self):
    # Getter method for a Coordinate object's x coordinate.
    # Getter methods are better practice than just accessing an attribute directly
    return self.x

  def getY(self):
    # Getter method for a Coordinate object's y coordinate
    return self.y
  
  def __str__(self):
    return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

  def eq(self):
    if self.getX==self.getY:
      return True
    else:
      return False
  
  def repr(self):
    ex="Coordinate("+str(self.getX())+","+str(self.getY())+")"
    return ex
    

obj=Coordinate(4,5)
print("Inside eq():"+str(obj.eq()))
print("Using eval() in repr():"+str(eval(repr(obj.eq()))))
print("Inside repr():"+obj.repr())
