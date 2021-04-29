"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
import time

from adafruit_circuitplayground import cp
while True:
#cp.pixels.fill((255,0,0))
#print ("Light:", cp.light)
#time.cleep(0.2)
#if (cp.light < 256):
  #  cp.pixels.fill((cp.light, cp.light, cp.light))


light=cp.light
if light % 32== 0 and cp.light !=0:
  light = light - 1
index =  light //32
