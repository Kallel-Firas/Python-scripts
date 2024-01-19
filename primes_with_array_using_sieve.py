from numpy import array, append

def is_prime(x):
    prime=-1
    for i in range(1,x,2):
        if not x%i:
            prime+=1
    return not prime


L=array([2])
for i in range(3,100,2):
    Is_Prime=True
    for j in L:
        if j>i**.5:break
        if not i%j:
            Is_Prime=False
            break
    if Is_Prime:
        L=append(L,i)
for i in L:
    print(i,end=" ' ")