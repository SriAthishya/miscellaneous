list1 =[10,20,40,40,50]
#o/p= [50,20,40,40,10]
print("I/p:"+str(list1))
op=[]
a=list1[0]
list1.remove(a)
op.append(list1.pop())
for i in list1:
  op.append(i)
op.append(a)
print("O/p:"+str(op))
