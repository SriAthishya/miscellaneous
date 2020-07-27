
def names(name):
  a=name.split()
  print("First name:"+a[0])
  print("Last name:"+a[1])

names("Sri Athishya")

def area_of_rec(l,b):
  area=l*b
  print(area)
l=6
b=7

area_of_rec(b,l)

def names(first,last):
  a=first+" "+last
  print(a)

names(last="Athishya",first="Sri")

def check_vowels(name,l1=['a','e','i','o','u']):
  count=0
  for i in l1:
    for j in name:
      if i==j:
        count+=1
  print(count)
check_vowels("athishya")

def mul(num):
  for i in range(1,num+1):
    mul=i*7
    print(str(i)+" * 7 = "+str(mul))

mul(7)