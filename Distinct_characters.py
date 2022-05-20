n=input()
l=n.lower()
s=l.split()
e=[]
for i in l:
    if i==' ':
        continue
    c=l.count(i)
    if(c==1):
        e.append(i)
e.sort()
for i in e:
    print(i,end="")