

from adafruit_clue import clue #importing clue in adafruit.
from time import sleep, time#importing sleep in time.
from random import randint #importing random numbers.


clue_display = clue.simple_text_display(title="REACTION GAME", title_scale=1, text_scale=2, title_color=clue.YELLOW)  #   display the REACTION GAME  with the corresponding color and  sized.

while True:                                         
    clue_display[0].text = "Instructions:"          # This code will display the text with its corrresponding color     
    clue_display[0].color = clue.GREEN               # and indexes. 
    clue_display[1].text = "Player 1 press A"                
    clue_display[1].color = clue.WHITE              
    clue_display[2].text = "Player 2 press B"
    clue_display[2].color = clue.WHITE
    clue_display[3].text = "Press if the number"
    clue_display[3].color = clue.BLUE
    clue_display[4].text = "is divisible by 2"
    clue_display[4].color = clue.BLUE
    clue_display[5].text = "Maximum score of 5"
    clue_display[5].color = clue.YELLOW
    
   
    for i in range (3, 0, -1):    # Loop that counts from 3 to 1 
        sleep(1)                     #time interval     
        clue_display[6].text = "Starts in " + str(i)        #display t he text and then convert the value of i into string so that it will display
        clue_display[6] .color = clue.ORANGE                  
       
        

        A_score = 0                                         # Declare a varible and set it into 0 (zero)               
        B_score = 0
      
        if i == 1:                                          # If the value of i is equal to 1  it will proceed the loop
            while True:                                     # infinite loop 
                num =  randint(1, 100)                      # declaring varaible that holds the random number
                clue_display[0].text = ""                   # From index 0 up until index 3 it will display empty phrase
                clue_display[1].text = "" 
                clue_display[2].text = "" 
                clue_display[3].text = ""
                clue_display[4].text = "Player A score: " + str(A_score)  # will display the text Player A score and the variable that we declare above 
                clue_display[5].text = "Player B score: " + str(B_score)  # which is A_score = 0 and B_score = 0
                clue_display[6].text = ""

                clue_display[1].text = "        " + str(num)    # HERE it will display the random number in index 1
            
            
                measure1 = time()                     #    declare 2 variable that equal to time
                measure2 = time()                     
                counter = 1                           #    declare variable counter that equal to 1

                while counter > 0:                    # loop that contains the condition if counter is greater than 0  
                    if measure2 - measure1 >= 1:      # after the loop meet the conditon it will proceed in this statements
                        counter = 0                   # variable counter set to zero
                    else:
                        measure2 = time()             
                    
                    if clue.button_a:                 #  statements if, once a button a is click and
                    
                        if num % 2 == 0:              # if  random number is modulo by 2 and equal to zero  
                            A_score +=1               # score will iterate by  1 
                        else:                      
                            A_score -=1               # else it will minus  1 
                        break

                    if clue.button_b:                 # IF BUTTON B is click and  random number is modulo by 2 
                        if num % 2 == 0:
                            B_score +=1               # score of B will iterate by 1
                        else:
                            B_score -=1               # else it will deducted by one
                        break
            
                if A_score == 5:                                # Statements that if A_score is equal to 5 it will display text 
                    clue_display[1].text = ""                   # in index 1 with a color red
                    clue_display[1].text = "PLAYER A WINS!"     # and break after meet the statements.
                    clue_display[1].color = clue.RED
                    break
                        

                if B_score == 5:                                # Statements that if B_score is equal to 5 it will display 
                    clue_display[1].text = ""                   # text in index 1 with a color red and it will will break after
                    clue_display[1].text = "PLAYER B WINS!"     # the statements will meet the condition.
                    clue_display[1].color = clue.RED
                    break
                       
        sleep(1)                                                # sleep in one second
        clue_display.show()     