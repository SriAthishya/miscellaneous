#Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person():
  def getgender(self):
    print("Person")
class Male(Person):
  def getgender(self,M):
    print("Male")

class Female(Male):
  def getgender(self,F):
    print("Female")

obj=Person()
obj.getgender()

obj0=Male()
obj0.getgender("Ram")

obj1=Female()
obj1.getgender("Sheela")