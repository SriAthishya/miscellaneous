#code to print the below pattern
def print_pattern(n):
  for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print("\r")
a=5
print_pattern(a)
print("--------------------")
print(" ")
#declare a list range(533,875) Try to count the number of odd and even numbers between the above range

print(" ")
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
odd_or_even(a=533,b=875)
print("----------")
print(" ")

#Credit card Code

cc_name=input("Enter the Credit Card Number: ")
name_=cc_name.find("_")
name=cc_name.find(" ")
cc_name=cc_name.replace(" ","")
cc_name=cc_name.replace("_","")
cc_name1=cc_name.replace("-","")
length=len(cc_name1)
strt=cc_name1[0]
digi=cc_name1.isdigit()
list1=[]
j=4
k=0
while j<length+4:
  spt=cc_name1[k:j]
  list1.append(spt)
  k+=4
  j+=4  
hifn="-".join(list1)
ck=cc_name.split("-")

pk=cc_name.find("-")

l=len(ck)
gk=0
for z in range(0,l):
  leng=len(ck[z])
  if pk!=-1:
    if leng==4:
      continue
    else:
      gk+=1
  elif pk!=-1:
    if leng==4:
      continue
    else:
      gk+=1
  else:
    gk=0   
a=0
while a<=length-4:
  b=a+1
  c=b+1
  d=c+1
  if cc_name1[a]==cc_name1[b]==cc_name1[c]==cc_name1[d]:
    s=True
    break    
  else:
    a+=1
    s=False 
if strt=='4' or '5' or '6' and length==16:
  if digi==True and name_==-1 and name==-1 and s==False and gk==0:
    print("Valid")
  else:
    print("Invalid")
else:
  print("Invalid")
  


  