al=int(input())
l=[]
for i in range(al):
    l.append(int(input()))
sn=int(input())
l.sort()
print(l[sn-1])