"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

from time import sleep 
from adafruit_circuitplayground import cp

led = 9
while True:

#kon ang rotation sa led or sa color sa led mo reach ug 10 mo balik sya sa index 0.
    if led == 10:
       led = 0
##kon ang rotation sa led or sa color sa led mo reach ug -1 mo balik sya sa index 9.

    if led == -1 :
       led = 9
    
#kani pra sa color sa LED
    cp.pixels[led] = (0, 0, 255)
    sleep(0.5)
    cp.pixels[led] = (0, 0, 0)
#para sa switch nga kon e click nimo ang false mo  rotate ang light sa left nga direction then if true kay mo rotate sya sa right direction
    if cp.switch:
        led += 1
    else:
        led -= 1

    



