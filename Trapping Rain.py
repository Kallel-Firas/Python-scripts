def calculate(T):
    '''
    first solution: run through the list from the right until the first occurence max then from the left until the same max index 
    '''
    i=1
    b=0
    stop=T.index(max(T))
    drops=0
    while b<stop:
        while i<stop and T[b]>T[i]:
            drops+=T[b]-T[i]
            i+=1
        b=i
        i+=1
    i=len(T)-1
    b=len(T)-1
    stop=T.index(max(T))
    while b>stop:
        while i>stop and T[b]>T[i]:
            drops+=T[b]-T[i]
            i-=1
        b=i
        i-=1
    print(drops)

def rain(blocks):
    '''
    second solution:
    run through the list from the left to the right, but must bisect the list where the first occurence of max is found and pass list[:max_index+1] then list[max_index:][::-1] to the function and add the results
    '''
    i=1
    b=0
    drops=0
    while b<len(blocks)-1:
        while i<len(blocks)-1 and blocks[b]>blocks[i]:
            drops+=blocks[b]-blocks[i]
            i+=1
        b=i
        i+=1
    return drops

T=[3,2,2,2,8,2,8,3,0,7,8,2,0,5]

calculate(T)
stop=T.index(max(T))
print(rain(T[:stop+1])+rain(T[stop:][::-1]))