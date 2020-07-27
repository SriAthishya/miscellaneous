#Find the max of consonents between 2 vowels
def fun(str0):
  a=""
  j=0
  l={}
  n=[]
  lt=['a','e','i','o','u']
  str0=str0.lower()
  for i in range(0,len(str0)):
    if str0[i] in lt:
      if len(a)==0:
        a=str0[i]
      else:
        str2=""
        coun=0
        str2=str0[j:i+1]
        a1=str0[i]
        coun=len(str2)-2
        l[coun]=str2
        a=a1
        
      j=i
  print(l)
  n=l.keys()
  num=max(n)
  print("Maximum alphabets between vowels is: "+l[num])
str1=input("Type a string:")
fun(str1)
