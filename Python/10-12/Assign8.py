#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 5000 and 7500 (both included)
def div7_not5(num1,num2):
  """Find numbers that are divisible by 7 and not by 5."""
  
  for i in range(num1,num2+1):
    if i%7==0 and i%5!=0:
      print(i,end=",")
      
  print(div7_not5.__doc__)

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
def list_tuple(inp):
  """Given numbers in list and tuple"""
  lt=[]
  for i in inp:
    if i.isalnum()==True:
      lt.append(int(i))
  print(tuple(lt))
  print(lt)
  print(list_tuple.__doc__)
  
#generate the Fibonacci series (val<200)
def fibonacci(val):
  """Fibonacci series"""
  num=0
  n1=0
  n2=1
  print(n1)
  while(num<=val):
    print(n2)
    num=n1+n2
    n1 = n2
    n2 = num
 
  print(fibonacci.__doc__)



