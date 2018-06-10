n=int(input())
s=[]
a=k=0
b=1
while s[:k]!=s[k:] or k<1:
    s+=[a%n]
    k=len(s)/2
    a,b=b,a+b
