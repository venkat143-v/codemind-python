n=int(input())
for i in range(1,n+1):
    a=int(input())
    l=list(map(int,input().split()))
    le=len(l)
    d=le//2
    f1=l[:d]
    f2=l[d:][::-1]
    e=[]
    l1=len(f1)
    l2=len(f2)
    i=0
    j=0
    while(i<l1 and j<l2):
        e.append(f2[j])
        e.append(f1[j])
        i+=1
        j+=1
    while(i<l1):
        e.append(f1[i])
        i+=1
    while(j<l2):
        e.append(f2[i])
        j+=1
    print(*e)