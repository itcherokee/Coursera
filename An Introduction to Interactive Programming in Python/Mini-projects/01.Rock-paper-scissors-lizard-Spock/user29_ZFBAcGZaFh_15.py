# Rock-paper-scissors-lizard-Spock template
import random

# helper functions
def name_to_number(name):
    result = None
    if name=="rock":
        result = 0
    elif name=="Spock":
        result = 1 
    elif name == "paper":
        result = 2
    elif name =="lizard":
        result = 3
    elif name =="scissors":
        result = 4
    else:
        print "Invalid input!"
    return result        

def number_to_name(number):
    result = None
    if number==0:
        result = "rock"
    elif number==1:
        result = "Spock" 
    elif number == 2:
        result = "paper"
    elif number ==3:
        result = "lizard"
    elif number ==4:
        result = "scissors"
    else:
        print "Invalid input!"
    return result 
    
# main function    
def rpsls(player_choice): 
    print
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    difference = (comp_number - player_number) % 5
    if difference == 0:
        print "Player and computer tie!"
    elif difference > 2:
        print "Player wins!"
    elif difference <= 2:
        print "Computer wins!" 
    else:
        print "Something goes terribly wrong in calculation!"
    
# Game run    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")