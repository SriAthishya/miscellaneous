class BubbleSort():
    def bubbleSort(self,list1):
        length = len(list1)
        for i in range(0,length-1):
            for j in range(0,length-i-1):
                if list1[j]>list1[j+1]:
                    list1[j],list1[j+1] = list1[j+1],list1[j]
if __name__ == '__main__':
   obj=BubbleSort()
   leng=int(input("The length of the list: "))
   print("Enter the numbers to be sorted: ")
   ip=[]
   while(leng!=0):
       val=int(input())
       ip.append(val)
       leng-=1
   obj.bubbleSort(ip)
   op=[]
   for i in range(0,len(ip)):
       op.append(ip[i])
   print("Numbers in sorted order: "+str(op))