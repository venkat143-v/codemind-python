n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))[:a]
    l2=list(map(int,input().split()))[:b]
    l1.extend(l2)
    l1.sort()
    print(*l1)