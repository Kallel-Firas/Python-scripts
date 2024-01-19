while True:
    ch = input('donner une chaine: ')
    if ch!='':
        break
nb_mots = 1
for i in ch:
    if i ==" ":
        nb_mots +=1
ch2 = ''
for i in range(len(ch)):
    car = ch[i].upper()
    if car ==" ":
        ch2 = ch2 +" "
    else:
        if (ord(car)-64 + nb_mots) > 26:
            rang = (ord(car)-64+nb_mots) % 26
        else:
            rang = ord(car)-64 + nb_mots
        if ch[i].isupper():
            ch2 = ch2 + chr(rang + 64)
        else:
            ch2 = ch2 + chr(rang+96)
print(ch2)