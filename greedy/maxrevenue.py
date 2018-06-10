#python3
n=input()
n=int(n)
a=[int(k) for k in input().split()]
b=[int(i) for i in input().split()]
v=[]
z=0
while len(v)<n:
    idx1=0
    idx2=0
    revenue=0
    for i in range(0,n-len(v)):
        for j in range(0,n-len(v)):
            if a[i]*b[j]>revenue:
                revenue=a[i]*b[j]
                idx2=j
                idx1=i
                continue
            continue
        continue
    v.append(revenue)
    b.pop(idx2)
    a.pop(idx1)
for k in v:
    z=z+k
print(z)

        
    
