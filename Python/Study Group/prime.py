num=int(input("Enter a number: "))
length=num-2
coun=0
if num>1:
    for i in range(2,num):
        if num%i!=0:
            coun+=1


if coun==length:
    print("This is prime number")
else:
    print("This is not prime number")