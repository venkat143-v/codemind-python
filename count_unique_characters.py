n=input()
l=n.lower()
e=[]
for i in l:
    if i==' ':
        continue
    c=l.count(i)
    if(c==1):
        e.append(i)
print(len(e))