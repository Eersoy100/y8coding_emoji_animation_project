x = chr(456)
from os import system
from time import sleep
clear = lambda : system("cls")


for i in range(20):
    print(" " * i, x)
    sleep(0.05)
    clear()
