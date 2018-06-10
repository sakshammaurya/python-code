#python3
z,m=input().split()
z=int(z)
m=int(m)
if z>m:
    big=z
    small=m
else:
    big=m
    small=z

modlist=[]
def fibmodulo(n:'upto n number')->int:
    if n<=0:
        return n
    a=0
    b=1
    fibo=[a,b]
    for i in range(0,n-1):
            b=a+b
            a=b-a
            c=b%10
    return c
d=0
for k in range(small,big+1):
    
    d=d+fibmodulo(k)

result=d%10
print(result)
