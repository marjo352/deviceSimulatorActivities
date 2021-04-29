from microbit import *
from time import sleep 

while True:
        for y in range (5): # this will access the index in horizontal axis
           for x in range (5):# thill access the index in vertical axis
                display.set_pixel(x, y, 9)#this will light up the pixel in maximum brightness of 9
                sleep (1) #sets the sleep
                display.set_pixel(x, y, 0)#ang purpose ani is para dili mag pa bilin nga ga siga ang pixel na execute before mo adto sa sunod nga pixel


       
       

    