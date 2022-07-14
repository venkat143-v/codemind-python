a,b=map(int,input().split())
e=[]
for i in range(a):
    l=list(map(int,input().split()))
    e.append(l)
for i in range(b):
    c=e[0][i]
    for j in range(a):
        if e[j][i]>c:
            c=e[j][i]
    print(c)
            