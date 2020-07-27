
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
for l in list1:
   num=l*10
   list2.append(num)
print(list2)
for m in list2:
   if(m%50==0):
       list3.append(m)
print(list3)