import requests
'''
resp=requests.get("https://www.google.co.in/",verify=False)
print(resp,dir(resp))
print(resp.url)
print(resp.content)

with open('google.html','w') as w_obj:
  w_obj.write(resp.text)
'''
def get_method(url):
  """ Download the page"""
  resp=requests.get(url,verify=False)
  if resp.status_code in [200,'200']:
      return(resp.content)
	   
def write_file(filename,data):
    """write the file"""
    with open(filename,'wb')as w_obj:
        w_obj.write(data)
        return True
    return False


def find_bullet(fn):
  list1=[]
  with open(fn,'rb')as r_obj:
      txt=r_obj.readlines()
  
  for i in txt:
    if b'<li>' in i and len(i)>25 and len(i)<=45:
      list1.append(i)
  for i in list1:
    import re
    clean = re.compile('<.*?>')
    l=re.sub(clean, '',str(i))
    #print(l)
    s=l[0:-3]
    print(s[2:])



data=get_method("http://en.wikipedia.org/wiki/Python_(programming_language)")
status=write_file("google.html",data)
find_bullet("google.html")
