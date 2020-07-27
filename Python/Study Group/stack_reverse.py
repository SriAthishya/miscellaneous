
str1="athishya"
str2=""
stact=[]
for i in str1:
    stact.append(i)
print(stact)
while len(stact)>0:
    str2=str2+stact.pop()
print(str2)