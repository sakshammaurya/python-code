#python3
a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    big=a
    small=b
else:
    big=b
    small=a
while True:
    k=big%small
    if k==0:
        gcd=small
        break
    elif k>0:
        big=small
        small=k
        continue
gcd=int(gcd)
lcm=int((a*b)//gcd)

print(lcm)
