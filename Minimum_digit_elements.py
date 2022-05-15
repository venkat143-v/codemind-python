n=int(input())
l=list(map(int,input().split()))
s=[]
o=[]
for i in l:
    a=str(i)
    le=len(a)
    s.append(le)
m=min(s)
for i in l:
    b=str(i)
    le=len(b)
    if(le==m):
        o.append(int(i))
print(len(o))