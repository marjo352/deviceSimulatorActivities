from microbit import * 
from time import sleep 


#declaring an array to access every index of the pixel 
#initializing variable spiral to hold the value of the corresponding indexes
spiral = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [4, 1], [4, 2], [4, 3], [4, 4], [3, 4],
    [2, 4], [1, 4], [0, 4], [0, 3], [0, 2],
    [0, 1], [1, 1], [2, 1], [3, 1], [3, 2],
    [3, 3], [2, 3], [1, 3], [1, 2], [2, 2]]

while True:    
    # range of the length of spiral starting from index 0
    for i in range(0, len(spiral)):
        # set the brightness of the LED to its maximum brightness 
        display.set_pixel(spiral[i][0], spiral[i][1], 9)
      
        # sleep for 1 interval
        sleep(1)
        #  set the brightness of the LED to its minimum brightness
        display.set_pixel(spiral[i][0], spiral[i][1], 0)
        