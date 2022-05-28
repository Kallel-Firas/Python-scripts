def nb_divisors(x):
    nb=1
    for i in range(2,x//2+1):
        if not x%i:
            nb+=1
    return nb+1

def maxi(x,y):
    if x>y:
        return True
    else:
        return False

l2=[]
biggest=0
for i in range(2,10000):
    l2+=[nb_divisors(i)]
    if maxi(l2[-1],biggest):
        print(i,l2[-1])
        biggest=l2[-1]
