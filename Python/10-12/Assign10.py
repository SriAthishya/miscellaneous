#Functions takes two inputs , first input is mandatory, if second is not there use 1, else if 0 raise error
def fun(n1,n2):
  """Function with two inputs"""
  if n1=='':
    print("First Parameter is mandatory")  
  elif n2=='':
    print("No Error")
  else:
    print("Error")
  print(fun.__doc__)
  
fun(4,'')
fun(3,5)
fun('',8)
print("----------------------------------")
print("")
#swapcase a string without using built in functions
def str_swapcase(str1):
  """Swapcase a string without build-in functions"""
  c=''
  print("The string is "+str1)
  for i in str1:
    a=ord(i)
    if a>96:
      b=a-32
      c+=chr(b)
      #print(c)
    elif a>64:
      b=a+32
      c+=chr(b)
  print("The swapcase string is "+c)
  print(str_swapcase.__doc__)

str_swapcase("aTHI")



#Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there? (i.e) "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"
import string

def is_abecedarian(str1):
  """returns True if the letters in a word appear in alphabetical order"""
  a=str1.lower()
  b=string.ascii_lowercase
  n1=0
  coun=0
  for i in a:
    if i in b :
      n2=ord(i)
      if n1<=n2:
        coun+=1
      else:
        print(str1+" not an abecedarian")
        return False
        break
    n1=n2 
  if coun==len(str1):
    print(str1+" is an abecedarian")
  print(is_abecedarian.__doc__)

is_abecedarian("Abhor")    
is_abecedarian("Aux")
is_abecedarian("Banana")
is_abecedarian("Aadil")
is_abecedarian("Athi")

print("----------------------------------")
print("")

#Write a function to convert Celsius to Fahrenheit and vice versa
def far_cel_conversion(deg):
  """Convert Fahrenheit to Celsius and Celsius to Fahrenheit"""
  d=int(deg[:-2])
  if deg.endswith("c"):
    f=(d*1.8)+32
    print(str(d)+" degree Celsius is equal to "+str(f)+" degree Fahrenheit")
  else:
    c=(d-32)/1.8
    print(str(d)+" degree Fahrenheit is equal to "+str(c)+" degree Celsius")
  
  print(far_cel_conversion.__doc__)

far_cel_conversion("23`c")
far_cel_conversion("106`c")
    

  