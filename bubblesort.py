def bub():
    T=[5,8,1,3,2,2]
    permute=True
    while permute==True:
        permute=False
        for i in range(len(T)-1):
            if T[i]>T[i+1]:
                temp=T[i]
                T[i]=T[i+1]
                T[i+1]=temp
                permute=True
    print(T)
bub()  