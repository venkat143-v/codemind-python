l=list(map(int,input().split()))
e=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        m=(l[i]-1)*(l[j]-1)
        e.append(m)
print(max(e))