from time import sleep 
from adafruit_circuitplayground import cp
  

  
while True:
    light = cp.light       
    if light % 32 == 0 and cp.light !=0:  
        light = light -1  # value sa light nga e produce
    index = light // 32 #e check niya kon asa sya nga index mo generate ug light
    if light > 32:
        light = light - (index * 32) 

    for i in range(0, 10): 
        if i == index : #if true ang condition mao ni ang e execute
             color = int(255 * light  / 32)
             
             cp.pixels[i] = (color, color, color)    
        elif i > index: 
            cp.pixels[i]= 0 # mo foff ang  light if mo go backward 
           
        else:
            cp.pixels[i] = 1
        