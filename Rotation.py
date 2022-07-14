n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))[:a]
    c=b%a
    if(c!=0):
        print(*l[-c:]+l[:a-c])
    else:
        print(*l)