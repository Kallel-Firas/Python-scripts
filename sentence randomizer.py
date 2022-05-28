from random import randint
l=input("Type a sentence:  ").split()
output=''
while l!=[]:
    output+=l.pop(randint(0,len(l)-1))+" "
print('\n',output)
