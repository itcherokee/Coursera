# Memory Game
import simplegui
import random

# helper functions 
def new_game():
    """ Initialize game """
    global deck, exposed, state, opened_cards, turns
    exposed = []					# creates exposed cards list
    for card in range(0,16):		# initialize exposed cards list
        exposed.append(False)    
    state = 0						# no card is opened
    turns = 0						# initialize turns' counter    
    deck = range(0,8) + range(0,8) 	# generate deck of numbers
    random.shuffle(deck)			# shuffle deck of numbers
    opened_cards = [-1,-1]			# initialize index of opened cards
    label.set_text('Turns = 0')
    
def clear_exposed_cards(value):
    """ Sets values of already exposed pairs/cards """
    """ value = False - cards are not pairs (equal); None - cards are pairs (same numbers) """
    exposed[opened_cards[0]] = value	
    exposed[opened_cards[1]] = value	 
    
def set_exposed_card(card_index, state):
    """ Sets all properties for currently opened card """
    exposed[card_index] = True            
    opened_cards[state] = card_index    
     
# event handlers
def mouseclick(pos):
    global exposed, opened_cards, state, turns
    card_index = pos[0] / 50			# calculate which card is clicked
    if exposed[card_index] != None:        
        if state < 2 or card_index in opened_cards:	            
            if not exposed[card_index]:	# card is not opened
                turns += 1 if state == 1 else 0	# increase turns on second opened card
                set_exposed_card(card_index, state)
                state +=1                        
        else:							# both cards are opened
            if deck[opened_cards[0]] == deck[opened_cards[1]]:	
                clear_exposed_cards(None) # pair cards found          
            else:						# opened cards are not pairs
                clear_exposed_cards(False)       
            set_exposed_card(card_index, 0)    
            opened_cards[1] = -1			
            state = 1            
                          
def draw(canvas):
    step = 800 / 16 						# = 50 - width of a card
    label.set_text('Turns = ' + str(turns))	# change counter label
    for index in range(16):		# loop through deck
        x1 = index * 50			# calculate left upper x-coord of current card
        x2 = (index + 1) * 50 	# calculate right upper x-coord of current card
        fill = 'Green' 			# set fill-in color of a card (to be used if card is not opened)
        text_color = 'White' if exposed[index] else 'Yellow'	# Sets number color depending does card is pair or not
        if exposed[index] or exposed[index] == None:			# checks does card is opened
            canvas.draw_text(str(deck[index]), [x1+15,60], 40, text_color)
            fill = None			#no fill-in color - card is exposed
        canvas.draw_polygon([[x1, 0], [x2, 0], [x2, 99], [x1, 99]], 5, 'Grey', fill)    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
