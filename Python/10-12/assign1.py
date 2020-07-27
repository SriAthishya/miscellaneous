name="sri Athishya Murugan"
print(name)

#capitalize
Name=name.capitalize()
print(Name)

#Center
center=Name.center(60,"-")
print(center)

#count
count=Name.count("a",0,-1)
print(count)

#endswith
end=Name.endswith("murugan")
end1=Name.endswith("murugan",10)
print(end)
print(end1)
end2=Name.endswith("ya",2,10)
print(end2)

#find
find=Name.find("athi",4)
print(find)

#index
index=Name.index("murug")
print(index)

#isalnum
name1="Athi20"
alnum=name1.isalnum()
print(alnum)

#isalpha
Name1="magic"
alpha=Name1.isalpha()
print(alpha)

#isdigit
n="123"
num=n.isdigit()
print(num)

#islower
low=Name1.islower()
print(low)

#isnumeric
numeric=n.isnumeric()
print(numeric)

#isspace
sp="   "
space=Name.isspace()
space1=sp.isspace()
print(space)
print(space1)

#istitle
name2="This Is Ball"
title=name2.istitle()
print(title)
title1=Name.istitle()
print(title1)

#isupper
up="BAT"
upper=up.isupper()
print(upper)

#join
s="->"
seq="a","b","c"
join=s.join(seq)
print(join)

#length
length=len(Name)
print(length)

#lower
lower=Name.lower()
print(lower)

#lstrip
str="123abc123"
trip=str.lstrip("123")
print(trip)

#max
ab="apple"
maxi=max(ab)
print(maxi)

#min
mini=min(ab)
print(mini)

#replace
replaced=ab.replace("p","P",1)
print(replaced)

#split
split=Name.split()
print(split)

#Startswith
start=Name.startswith("athi",4,15)
print(start)

#swapcase
swap=name.swapcase()
print(swap)

