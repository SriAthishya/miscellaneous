def anagram(str1,str2):
	str1r={}
	str2r={}
	count=0
	for i in str1:
	  a=ord(i)
	  str1r[a]=i
	for i in str2:
	  b=ord(i)
	  str2r[b]=i
	for i in str1r.keys():
	  for j in str2r.keys():
        if i == j:
            count+=1
	if count==len(str1):
	  print(str1+" and "+str2+" is Anagram")
	else:
	  print(str1+" and "+str2+" is not Anagram")
  
str1="earth"
str2="heart"
anagram(str1,str2)
