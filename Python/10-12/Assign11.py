class Full_Name():
  def lower(self,name):
    
    """LowerCase of name"""
    try:
        a=name.lower()
        return a
    except Exception as E:
        return E
        
      
  
  def upper(self,name):
    
    """UpperCase of name"""
    try:
        a=name.upper()
        return a
        
    except Exception as e:
        return e

  def split_name(self,name):
    
    """Split name"""
    try:
        a=name.split(" ")
        a=",".join(a)
        return a
    except Exception as e :
        return e

  def find_vowels(self,name):
    
    """Number of Vowels in the name"""
    try:
        coun=0
        for i in name:
          if i in ['a','e','i','o','u','A','E','I','O','U']:
            coun+=1
        return coun
    except Exception as e:
        return e

ob=Full_Name()
full_name=input("Enter your Full Name: ")
print(ob.lower.__doc__+" : "+ob.lower(full_name))
print(ob.upper.__doc__+" : "+ob.upper(full_name))
print(ob.split_name.__doc__+" : "+str(ob.split_name(full_name)))
print(ob.find_vowels.__doc__+" : "+str(ob.find_vowels(full_name)))

print("")
print("----------------------------------------------------------------------------------")
print("")

class Function():

  def is_sorted(self,lt):
    
    """Check is the elements in the list are sorted or not"""
    try:
        j=1
        coun=0
        for i in range(0,len(lt)-1):
          if lt[i]<lt[j]:
            coun+=1
          else:
            continue
          j+=1
        if coun==len(lt)-1:
          return True
        else:
          return False
    except Exception as E:
        return E
    

obj=Function()
list1=[1,3,9,12,34,56]
list2=[2,4,1,5,8]
list3=['a','b','c']
list4=['h','l','a',]
print(obj.is_sorted.__doc__+" : "+str(obj.is_sorted(list1)))
print(obj.is_sorted.__doc__+" : "+str(obj.is_sorted(list2)))
print(obj.is_sorted.__doc__+" : "+str(obj.is_sorted(list3)))
print(obj.is_sorted.__doc__+" : "+str(obj.is_sorted(list4)))