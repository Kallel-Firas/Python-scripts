from time import sleep
from keyboard import is_pressed, press_and_release
while True:
    while True:
        if is_pressed("1"):break
    while True:
        press_and_release("w")
        press_and_release("a")
        press_and_release("d")
        sleep(0.1)
        if (is_pressed("0")):break