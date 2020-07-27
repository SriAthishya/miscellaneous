#write a code to check if 'coffee' is present in the string 'I drink coffee every morning'
print("""code to check if 'coffee' is present in the string 'I drink coffee every morning'""")
print(" ")
def check_word(sentence):
    coffee="coffee"
    check=sentence.split()
    print(check[0]==coffee)
    print(check[1]==coffee)
    print(check[2]==coffee)
    print(check[3]==coffee)
    print(check[4]==coffee)
   
sentence='I drink coffee every morning'   
check_word(sentence)
print("------------------------------------")
print("     ")
#print the alphabet after the first occurrence of ',' from the below String 'I like python ,Perl scripting'
print("""print the alphabet after the first occurrence of ',' from the below String'I like python ,Perl scripting'""")
print("   ")

def find_and_display(sentence_1):
  trim=sentence_1.split()
  #trim=" ".join(trim)
  print(trim)
  select0=trim[0].startswith(',')
  print(select0)
  select1=trim[1].startswith(',')
  print(select1)
  select2=trim[2].startswith(',')
  print(select2)
  select3=trim[3].startswith(',')
  print(select3)
  select4=trim[4].startswith(',')
  print(select4)
  print(" ")
  if select3==True:
    print(trim[3][1:])

sentence_1='I like python ,Perl scripting'
find_and_display(sentence_1)
print("------------------------------------")
print("     ")
#get your full name and convert the first and middle name as abbreviations
print("get your full name and convert the first and middle name as abbreviations")
print(" ")
def initial_of_name(name):
  name1=name.split()
  nm=name1[0][0]
  nm1=name1[1][0]
  nm2=name1[2]
  name2=[]
  name2.append(nm)
  name2.append(nm1)
  name2.append(nm2)
  new=".".join(name2)
  print(new)

name="Sri Athishya Murugan"
initial_of_name(name)
print("------------------------------------")
print("     ")
#count the no. of whitespaces --> ": vect1 and vect2 are lists of equal length of numbers"
print("""count the no. of whitespaces --> ": vect1 and vect2 are lists of equal length of numbers""")
print(" ")
def count_of_space(sentence):
  splt=sentence.split()
  spce=len(splt)-1
  print(spce)

con=": vect1 and vect2 are lists of equal length of numbers"
count_of_space(con)
print("------------------------------------")
print("     ")
#i have a string -> str1 = "PYnative" - Use Slicing to get the output something like this --> Yna PYnat tive PYnativ PYnativ
print("""i have a string -> str1 = "PYnative" - Use Slicing to get the output something like this --> Yna PYnat tive PYnativ PYnativ""")
print(" ")
def trim(str1):
  str2=str1[1:4]
  str3=str1[0:5]
  str4=str1[4:]
  str5=str1[0:-1]
  print(str2+" "+str3+" "+str4+" "+str5+" "+str5)
word='PYnative'
trim(word)