str1='Hi my name is reeta'
str2='my friend name is anitha'
a=(str1.split(" "))
b=(str2.split(" "))
l=[]
for i in a:
    if i not in b:
        l.append(i)
for i in b:
    if i not in a:
        l.append(i)
print(l)

