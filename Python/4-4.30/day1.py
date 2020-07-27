#Find the sum of numbers in the list
list1 = [[1,2,3],4,[5,6]]
sum=0
lt=[]
for i in list1:
  if type(i)==list:
    for j in range(0,len(i)):
      sum+=i[j]
  else:
    sum+=i
    #print(sum)
  
print(sum)
print("")
print("----------------------------------")
print("")
#swapcase of the given string

str1 = "aBcDEFz"
str2=""
for i in str1:
  if i.upper()==i:
    i=i.lower()
  else:
    i=i.upper()
  str2=str2+i
print(str1+"---"+str2)


str1 = "aBcDEFz"
str2=""
for i in str1:
  a=ord(i)
  if a>90:
    b=a-32
  else: 
    b=a+32
  str2=str2+chr(b)
print(str1+"---"+str2)
