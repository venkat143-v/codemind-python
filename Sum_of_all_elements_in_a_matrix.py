def soaeim(n,m):
    s=0
    for i in range(1,n+1):
        l=list(map(int,input().split()))[:m]
        for i in l:
            s=s+i
    return(s)
n,m=map(int,input().split())
print(soaeim(n,m))