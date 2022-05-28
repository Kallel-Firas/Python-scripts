def primes_until(n):
    global T
    T=[True]*(n+1)
    T[0]=False
    T[1]=False
    for i in range(2,n+1):
        if T[i]:
            for j in range(2*i,n+1,i):
                T[j]=False
    
def factor(n):
    print(T)

primes_until(100)
factor(101)