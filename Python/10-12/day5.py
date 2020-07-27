#program1 to capitalize name
s=input("Enter the Name:")
list1=[]
for i in s:
  if( i.isalnum()==True or i.isalpha()==True):
    continue
spt=s.split()
for j in range(0,len(spt)):
  cap=spt[j].capitalize()
  list1.append(cap)
name=" ".join(list1)
print(name)
print("--------------------------------------"


#program to alter list


list1=[]
list3=[]
n=int(input("The number of commands: "))
list2=["insert","print","append","remove","sort","pop","reverse"]
#list1=random.choices(list2,k=n)
for i in range(0,n-1):
  if(list2[i]=="insert"):
    list1=((input("insert ").split()))
    list3.insert(int(list1[0]),int(list1[1]))
  elif(list2[i]=="print"):
    print(list3)
  elif(list2[i]=="remove"):
    rmv=int(input("remove "))
    list3.remove(rmv)
    print(list3)
  elif(list2[i]=="append"):
    app=int(input("append "))
    list3.append(app)
    print(list3)
  elif(list2[i]=="sort"):
    print("sort ")
    list3.sort()
    print(list3)
  elif(list2[i]=="pop"):
    print("pop ")
    list3.pop()
    print(list3)
  elif(list2[i]=="reverse"):
    print("reverse ")
    list3.reverse()
    print(list3)
  

