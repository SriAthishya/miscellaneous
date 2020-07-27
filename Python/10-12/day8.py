#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.Suppose the following input is supplied to the program
def count_of(sentence):
  low=0
  up=0
  
  for i in range(0,len(sentence)):
    if sentence[i].islower()==True:
      low+=1
    elif sentence[i].isupper()==True:
      up+=1
  print("Lower case = "+str(low))
  print("Upper Case = "+str(up))
  

def initial_of_name(name):
  name1=name.split()
  nm=name1[0][0]
  nm1=name1[1][0]
  nm2=name1[2]
  name2=[]
  name2.append(nm)
  name2.append(nm1)
  name2.append(nm2)
  new=".".join(name2)
  print(new)
 
def check_word(sentence):
    coffee="coffee"
    check=sentence.split()
    print(check[0]==coffee)
    print(check[1]==coffee)
    print(check[2]==coffee)
    print(check[3]==coffee)
    print(check[4]==coffee)
    
def find_and_display(sentence_1):
  trim=sentence_1.split()
  #trim=" ".join(trim)
  print(trim)
  select0=trim[0].startswith(',')
  print(select0)
  select1=trim[1].startswith(',')
  print(select1)
  select2=trim[2].startswith(',')
  print(select2)
  select3=trim[3].startswith(',')
  print(select3)
  select4=trim[4].startswith(',')
  print(select4)
  print(" ")
  if select3==True:
    print(trim[3][1:])
    
def count_of_space(sentence):
  splt=sentence.split()
  spce=len(splt)-1
  print(spce)

def trim(str1):
  str2=str1[1:4]
  str3=str1[0:5]
  str4=str1[4:]
  str5=str1[0:-1]
  print(str2+" "+str3+" "+str4+" "+str5+" "+str5)
  
def print_pattern(n):
  for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print("\r")

def odd_or_even(a,b):
  odd=0
  even=0
  for i in range(a,b):
    if i%2==0:
      even+=1
    else:
      odd+=1
  print("The number of odd numbers between 533 and 875 is: "+str(odd))
  print("The number of even numbers between 533 and 875 is: "+str(even))
  
def mul_of_7(num):
  for i in range(1,num+1):
    mul=i*7
    print(str(i)+" * 7 = "+str(mul))


def find_positive_negative(lt):
  count=0
  coun=0
  for i in lt:
    if(lt[i]>0):
      count+=1
    else:
      coun+=1
  print("Count of Positive numbers: "+str(count))
  print("Count of Negative numbers: "+str(coun))

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
  
def names(name):
  a=name.split()
  print("First name:"+a[0])
  print("Last name:"+a[1])


def area_of_rec(l,b):
  area=l*b
  print(area)




def names(first,last):
  a=first+" "+last
  print(a)



def check_vowels(name,l1=['a','e','i','o','u']):
  count=0
  for i in l1:
    for j in name:
      if i==j:
        count+=1
  print(count)


def mul(num):
  for i in range(1,num+1):
    mul=i*7
    print(str(i)+" * 7 = "+str(mul))

def sumDigits(s):
  sum=0
  for i in range(0,len(s)):
    if(s[i].isdigit()==True and s[i].isalnum()==True):
      sum+=int(s[i])
  print("Sum_of_digits = "+str(sum))




def isPalindrome(s):
  if s.isalpha()==True:  
    s=s.lower()
    rev_s=s[::-1]
    if rev_s==s:
      print("True")
    else:
      print("False")
  else:
      print("False")




def bin_to_dec(num):
  if num.isdigit()==True:
    num_len=len(num)
    con=0
    sum=0
    for i in range(0,num_len):
      if num[i]!='0' and num[i]!='1':
        print(num+" is not a binary number")
        exit()
      else:
        con=int(num[i])*(2**(num_len-1))
        num_len-=1
        sum+=con
  print("The decimal number of "+num+" is "+str(sum))






