#merge two dictionaries
def merge_dic(dic1,dic2):
  merge={**dic1,**dic2}
  return merge
dic1={'a':1,'b':2,'c':3}
dic2={'d':4,'e':5,'f':6}
print(merge_dic(dic1,dic2))
print("--------")
print("")
'''Assumes s is a string returns the sum of the decimal digits in
s for example, if s is 'a2b3c' it returns 5'''

def sumDigits(s):
  sum=0
  for i in range(0,len(s)):
    if(s[i].isdigit()==True and s[i].isalnum()==True):
      sum+=int(s[i])
  print("Sum_of_digits = "+str(sum))

sumDigits("a2b3c4")
print("--------")
print("")
"""Assumes s is a str returns True if s is a palindrome;False otherwise.Punctuation marks, blanks, and capitalization are ignored"""

def isPalindrome(s):
  if s.isalpha()==True:  
    s=s.lower()
    rev_s=s[::-1]
    if rev_s==s:
      print("True")
    else:
      print("False")
  else:
      print("False")

isPalindrome("123321")
print("--------")
print("")
#Binary to decimal conversion

def bin_to_dec(num):
  if num.isdigit()==True:
    num_len=len(num)
    con=0
    sum=0
    for i in range(0,num_len):
      if num[i]!='0' and num[i]!='1':
        print(num+" is not a binary number")
        exit()
      else:
        con=int(num[i])*(2**(num_len-1))
        num_len-=1
        sum+=con
  print("The decimal number of "+num+" is "+str(sum))

bin_to_dec("101")


