# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:41:04 2019

@author: tsharris
"""

#----------------------------Function definitions-------------------------
def displayDude(chances):
    if (chances==6):
        print ("--------")
        print ("|      |")
        print ("|     ")
        print ("|      ")
        print ("|     ")
        print ("|")
        print ("--------")
    elif (chances==5):
        print ("--------")
        print ("|      |")
        print ("|      O")
        print ("|      ")
        print ("|     ")
        print ("|")
        print ("--------")
    elif (chances==4):
        print ("--------")
        print ("|      |")
        print ("|      O/")
        print ("|      ")
        print ("|     ")
        print ("|")
        print ("--------")
    elif (chances==3):
        print ("--------")
        print ("|      |")
        print ("|     \\O/")
        print ("|      ")
        print ("|     ")
        print ("|")
        print ("--------")
    elif (chances==2):
        print ("--------")
        print ("|      |")
        print ("|     \\O/")
        print ("|      |")
        print ("|     ")
        print ("|")
        print ("--------")
    elif (chances==1):
        print ("--------")
        print ("|      |")
        print ("|     \\O/")
        print ("|      |")
        print ("|       \\")
        print ("|")
        print ("--------")
    elif (chances==0):
        print ("--------")
        print ("|      |")
        print ("|     \O/")
        print ("|      |")
        print ("|     / \\")
        print ("|")
        print ("--------")







#----------------------------Main program-------------------------

answer = "pneumonoultramicroscopicsilicovolcanoconiosis"
visible = ['_'] * len(answer)
life = 6  # number of chances you get

count = 0

while(True):
    print("*************************")
    displayDude(life)
    print(visible)
    print("You have", life,"chances left")
    
    guess = input("Guess a letter:")
    
    #check to see if the letter is in the answer
    found = False #not found
    for i in range(0, len(answer), 1): #check each index position
        if (answer[i] == guess):#if any index has the guess
            visible[i] = guess#make the guess visible
            count = count + 1 #one less letter to guess
            found = True #found
    
    if (found == False): #letter not found
        life = life - 1 #miss
        if (life==0):
            print ("You lose!")
            displayDude(0)
            break
    else:
        #check to see if the user has the entire word
        if (count == len(answer)):#if there are no blanks 
            print ("You win!")
            break
            
print("Game over!")
    
    
    
    
    