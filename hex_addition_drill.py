from random import randint

while True:
    n1 = randint(1, 16)
    n2 = randint(1, 16)
    n3 = hex(n1 + n2)
    print(f" {hex(n1)}")
    print(f"+{hex(n2)}")
    answer = hex(input())
    if answer == n3:
        print("Correct!")
    else:
        print(f"Wrong! correct answer is {n3}")
