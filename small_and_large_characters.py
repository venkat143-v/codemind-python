n=input()
s=n.split()
e=[]
for i in s:
    m=min(i)
    e.append(m)
    ma=max(i)
    e.append(ma)
print(*e)