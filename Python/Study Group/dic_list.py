mydict = [{'name': 'Roshni', 'marks': [10, 10, 10, 10, 20]}, {'name': 'Arun', 'marks': [10, 9, 8, 10, 20]}]
for i in mydict:
    for a,b in i.items():
        if type(b)==list:
            sum=0
            for c in b:
                sum+=c
            i[a]=sum
            print(i)
