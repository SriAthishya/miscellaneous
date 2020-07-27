with open("C:\\Users\\Sri Athishya\\Desktop\\Python\\Assign8.py",'r') as a_obj:
    out=a_obj.readlines()
    
    for lines in out:
        if 'def' in lines:
            fn=lines.split(" ")
            fn1=fn[1][:-2]
            fn2=fn1.split("(")
            print(fn2[0])