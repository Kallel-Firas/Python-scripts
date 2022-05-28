def convToBin(n):
    r=''
    while n!=0:
        r=str(n%2)+r
        n=n//2
    if r=='':
        print(0)
    else:
        print(r)

def convToOct(n):
    r=''
    while n!=0:
        r=str(n%8)+r
        n=n//8
    if r=='':
        print(0)
    else:
        print(r)

def convToHex(n):
    r=''
    while n!=0:
        if n%16>9:
            r=chr(n%16+55)+r
        else:
            r=str(n%16)+r
        n=n//16
    if r=='':
        print(0)
    else:
        print(r)

def convFromBin(n):
    n=str(n)
    res=0
    for i in range(len(n)):
        res=res+int(n[len(n)-1-i])*(2**i)
    print(res)
        


def convFromOct(n):
    n=str(n)
    res=0
    for i in range(len(n)):
        res=res+int(n[len(n)-1-i])*(8**i)
    print(res)

def convFromHex(n):
    n=str(n)
    res=0
    for i in range(len(n)):
        if n[len(n)-1-i]>='A':
            res=res+int(ord(n[len(n)-1-i])-55)*(16**i)
        else:
            res=res+int(n[len(n)-1-i])*(16**i)
    print(res)
