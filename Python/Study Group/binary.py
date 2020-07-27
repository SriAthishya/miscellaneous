num="101010"
flag=0
for i in num:
  if i=="0" or i=="1":
    flag+=1

if flag==len(num):
  print(num+" is binary number")
else:
  print(num+" is not a binary number")

s=[5,6,7,8]
m=0
for i in s:
  m+=i
print(m)
s = '1001000011'
# s+=str(0)
news = n = ""
maxx = 0
for i in s:
    if (i == '0'):
        n += str(i)
    else:
        if (len(n) > maxx):
            maxx = len(n)
            news = n
        n = ""
print(news)



