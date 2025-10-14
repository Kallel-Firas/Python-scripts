import sys
if len(sys.argv) != 2 or not sys.argv[1].isdecimal() or sys.argv[1] == '0':
    print(f"Usage: python3 {sys.argv[0]} <positive integer>"")
    exit(1)

def primes_until(n):
    global T
    T=[True]*(n+1)
    T[0]=False
    T[1]=False
    for i in range(2,n+1):
        if T[i]:
            for j in range(2*i,n+1,i):
                T[j]=False
    print([i for i in range(n+1) if T[i]])
    
primes_until(int(sys.argv[1]))
