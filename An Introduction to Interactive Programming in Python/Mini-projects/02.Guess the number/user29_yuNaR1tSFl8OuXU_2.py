# "Guess the number" mini-project
import simplegui
import random
import math

low = 0
high = 100
secret = 0
count = 0
win_moves = 0

def remaining_guesses():
    print "Number of remaining guesses is", win_moves - count
        
def new_game():    
    print "\nNew game. Range is from", low, "to", high
    global secret, win_moves, count
    count = 0
    secret = random.randrange(low,high)
    seq = high - (low+1)
    win_moves = int(math.ceil(math.log(seq)/math.log(2)))
    remaining_guesses()
    
def range100():
    global high
    high = 100    
    new_game()
    
def range1000():
    global high
    high = 1000
    new_game()
    
def input_guess(guess):	
    if guess == "" or not(guess.isdigit()):
        print "\nInvalid input! Game starts over!"
        new_game()
        return
    print "\nGuess was", guess  
    global count
    count = count + 1    
    remaining_guesses()
    guess_number = int(guess)    
    if count == win_moves:	
        print "You ran out of guesses. The number was", secret
        new_game()
        return  
    if guess_number == secret:
        print "Correct!"
        new_game()
        return
    elif guess_number < secret:
        print "Higher!"
    else:
        print "Lower!"

frame = simplegui.create_frame("Guess the number",200,200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

new_game()
frame.start()