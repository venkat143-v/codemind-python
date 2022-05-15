m,k=map(int,input().split())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if(i<0):
        i=i*-1
    s=str(i)
    e.append(s)
for i in e:
    le=len(i)
    if(le==k):
        o.append(i)
print(len(o))