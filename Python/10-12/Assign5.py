#iterate the list and store those values into 3 different lists one for int, one for str and one list for float values
print("")
def seperate_lists(list1):
  String=[]
  Integer=[]
  Float=[]
  for i in range(0,len(list1)):
    a=str(type(list1[i]))
    if('int' in a):
      Integer.append(list1[i])
    elif('str' in a):
      String.append(list1[i])
    elif('float' in a):
      Float.append(list1[i])
  print("Strings: "+str(String))
  print("Integers: "+str(Integer))
  print("Floats: "+str(Float))
list1=[1,'string',9.3,7,6.1,"Apple","Bunch",8,5.5]
seperate_lists(list1)
print("------------------")
print("")
#cube of the number
inp=0
while inp>=0:
  print("Enter the number or q: ")
  inte=(input())
  if(inte!='q'):
    inte=int(inte)
    cube=inte*inte*inte
    print("Cube of "+str(inte)+" is "+str(cube))
  else:
    print("quit")
    break
  inp+=1

