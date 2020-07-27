url = 'My Profile : https://google.com in the portal of https://expressbeats.accenture.com/'
l=[]
for i in url:
    a=(",").join(url.split(" "))
    for b in a:
        c=(a.split(","))
for i in c:
    if i.startswith("https"):
        l.append(i)
print(l)
