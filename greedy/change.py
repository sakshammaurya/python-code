#python3
m=int(input())
k=0
g=0
h=0
if m>=10:
    k=int(m/10)
    m=m%10
if 5<=m<10:
    g=int(m/5)
    m=m%5
if 1<=m<5:
    h=m

print(k+h+g)
