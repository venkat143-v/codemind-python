s=input()
l=s.lower()
m=s.split()
e=[]
o=[]
for i in m:
    c=0
    for j in i:
        if j=='a'or j=='e' or j=='i' or j=='o' or j=='u':
            c+=1
    e.append(c)
mi=min(e)
for k in m:
    s=0
    for d in k:
        if d=='a' or d=='e' or d=='i' or d=='o' or d=='u':
            s+=1
    if(mi==s):
        o.append(k)
print(len(o))