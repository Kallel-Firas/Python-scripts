#a ball is thrown form a certain distance and each time it hits the ground, it loose a fifth of its height
#the program will calculate how many times the ball hits the ground before its hight is less than 0.01

L=100
tbambiet=0
while .01<=L:
    print(L)
    L=L-(L/5)
    tbambiet=tbambiet+1
print("tbambiet =",tbambiet)