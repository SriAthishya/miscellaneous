#multiplication table for 7 table
def mul_of_7(num):
  for i in range(1,num+1):
    mul=i*7
    print(str(i)+" * 7 = "+str(mul))
num=int(input("Enter a number: "))
mul_of_7(num)
print("-----------------------------")
print(" ")
# To get to the count of negative, positive values from list
def find_positive_negative(lt):
  count=0
  coun=0
  for i in lt:
    if(lt[i]>0):
      count+=1
    else:
      coun+=1
  print("Count of Positive numbers: "+str(count))
  print("Count of Negative numbers: "+str(coun))

lt=[-4,3,1,6,-7,0,-9,-1,5]
find_positive_negative(lt)
