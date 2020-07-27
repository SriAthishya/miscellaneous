#Palindrome
import unittest

class check_palindrome(unittest.TestCase):
    def palin(self,str1):
        a=len(str1)//2
        for i in range(0,a):
          for j in range(-1,a):
            
            if str1[i]==str1[j]:
              self.assertEqual("Palindrome","Palindrome")
              return  "Palindrome"
            else:
              self.assertraises("Not Palindrome","Not Palindrome")
              return "Not Palindrome"

    
 
    
    #Matrix Multiplication
    def matrix_mul(self,m1,m2):
        for i in range(len(m1)):
            for j in range(len(m2)):
              for k in range(len(m3)):
                m3[i][j]+=m1[i][k]*m2[k][j]
        print("Matrix Multiplication:")

        for r in m3:
            print(r)
        

    #Matrix Addition
    def matrix_add(self,m1,m2):
        for i in range(len(m1)):
            for j in range(len(m2)):
              m4[i][j]=m1[i][j]+m2[i][j]
        print("Matrix Addition:")
        
        for r in m4:
            print(r)
            
        #return m4


    #display letters after last vowel of the string
    def string(self,str10):
        lt=[]
        for i in range(0,len(str10)):
            if str10[i] in "aeiou":
                lt.append(i)
        j=max(lt)+1
        str12=str10[j:]
        print("String After "+str10[max(lt)]+" is "+str12)
       
str2="abba"
m1=[[2,2],
    [1,1]]
m2=[[3,3],
    [1,1]]
m3=[[0,0],
    [0,0]]
m4=[[0,0],
    [0,0]]
str11="string"
obj=check_palindrome()
print(obj.palin(str2))
obj.matrix_add(m1,m2)
obj.matrix_mul(m1,m2)
obj.string(str11)
if __name__ == '__main__': 
    unittest.main()