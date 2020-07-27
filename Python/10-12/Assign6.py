stud={'Athi':{'class':11,'subject':{'science':95,'maths':99,'social':89}},
'Bala':{'class':10,'subject':{'science':96,'maths':89,'social':70}},
'Charu':{'class':9,'subject':{'science':99,'maths':89,'social':89}},
'Dinesh':{'class':10,'subject':{'science':79,'maths':78,'social':96}},
'Eunice':{'class':12,'subject':{'science':89,'maths':100,'social':78}}}

c={}
for i,j in stud.items():
  for a,b in j.items():
    if a=='subject':
      sum=0
      for d in b.values():
        sum+=d
      avg=sum//3
      c[i]=avg
  print("Average score of "+i+" is : "+str(avg))
max=0
name=""
print("")
for x,y in c.items():
  if y>max:
    max=y
    name=x
print(name+" has the maximum marks of "+str(max))