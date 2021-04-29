
from adafruit_clue import clue
from time import sleep

clue_data = clue.simple_text_display(title="Message Streamer", title_color=clue.RED, title_scale=2)
#declaring variables that holds the string 
message1 = "This message moves from right to left... "
message2 = "This message moves from left to right... "
message3 = "This message blinks"
while True:

    #message from right to left
    clue_data[1].text = message1 #getting the message1 and display it in index 1
    clue_data[1].color = clue.YELLOW #setting the color
    sleep(.02) #time interval
    temp1 = message1[0:1]
    message1 = message1[1:] + temp1
    #message from left to right
    clue_data[4].text = message2 #getting the message2 and display it in index 4
    clue_data[4].color = clue.WHITE #setting the color
    sleep(.02) #time interval
    temp2 = message2[len(message2) - 1]
    message2 = temp2 + message2[:-1]
    
    # blink
    clue_data[6].text = message3 #getting the message3 and display it in index 6
    clue_data[6].color = clue.BLUE #setting the color
    sleep(.02) #time interval
    clue_data[6].color = clue.BLACK

    clue_data.show()



