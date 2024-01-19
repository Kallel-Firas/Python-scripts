x1,y1,h1,w1=[int(j) for j in input().split()]
x2,y2,h2,w2=[int(j) for j in input().split()]
a,a1=[x1,y1],[x1+w1,y1+h1]
b,b1=[x2,y2],[x2+w2,y2+h2]
Simple=w1*h1+w2*h2
Common1=(h1-b[1]+a[1])*(w1-b[0]+a[0])
Common2=(h2-a[1]+b[1])*(w2-a[0]+b[0])
Area1=Simple-Common1
Area2=Simple-Common2
if a1[0]>=b1[0] and b[0]>=a[0] and a1[1]>=b1[1] and b[1]>=a[1]:print(w1*h1)
elif b1[0]>=a1[0] and a[0]>=b[0] and b1[1]>=a1[1] and a[1]>=b[1]:print(w2*h2)
elif a1[0]>=b[0] and a1[1]>=b[1]:
    if Area1>=0:print(Area1)
    else:print(Area2)
else:print(Simple)