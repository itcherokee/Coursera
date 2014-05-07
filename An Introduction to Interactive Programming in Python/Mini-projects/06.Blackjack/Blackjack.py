# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
card_size = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
win = 0
loss = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Classes
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        result = "Hand contains "
        for card in self.cards:
            result += card.suit + card.rank + " "
        return result    

    def add_card(self, card):
        if card != None:
            self.cards.append(card)

    def get_value(self):
        hand = 0
        ace = False
        for card in self.cards:
            if card.rank == 'A':
                ace = True
            hand += VALUES[card.rank]
        if hand <= 11 and ace:
            hand += 10
        return hand
   
    def draw(self, canvas, pos, who):
        dealer_first_card = True
        cards_face = card_images
        for card in self.cards:
            if who == "dealer" and dealer_first_card and in_play:
                dealer_first_card = False
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                              [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)
            else:
                card_loc = (card_size[0] * (0.5 + RANKS.index(card.rank)), card_size[1] * (0.5 + SUITS.index(card.suit)))
                canvas.draw_image(card_images, card_loc, card_size, 
                              [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)
            pos[0] += card_size[0] + 5
 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(len(RANKS)):
                one_suit = Card(SUITS[suit],RANKS[rank])
                self.deck.append(one_suit)

    def shuffle(self):
        random.shuffle(self.deck)            

    def deal_card(self):
        return self.deck.pop(0)
    
    def __str__(self):
        result = "Deck contains "
        for card in range(len(self.deck)):
            result += self.deck[card].suit + self.deck[card].rank + " "
        return result 
    
# Event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score, dealer_result, loss
    if in_play:
        outcome = 'Player - You have busted (DEAL button pressed)! New Deal?' 
        score -= 1
        loss += 1
        in_play = False
    else:    
        deck = Deck()
        deck.shuffle()
        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        in_play = True
        outcome = "Player - Hit or Stand?"
        dealer_result = 'Dealer'

def hit():
    global in_play, score, outcome, dealer_result, loss
    if in_play and player.get_value() <= 21:
        player.add_card(deck.deal_card())   
    if player.get_value() > 21:
        outcome = 'Player - You have busted! New Deal?'  
        if in_play: 
            score -= 1
            loss += 1
        in_play = False
        dealer_result = 'Dealer - hand value: ' + str(dealer.get_value())    
    
def stand():
    global in_play, score, outcome, dealer_result, loss, win
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())    
        if dealer.get_value() > 21:
            outcome = 'Dealer - Have been busted! New Deal?'  
            score +=1
            win += 1
            in_play = False
        elif player.get_value() <= dealer.get_value():
            outcome = 'Player - You have busted! New Deal?'   
            score -= 1
            loss += 1
            in_play = False
        else:	
            outcome = 'Dealer - Have been busted! New Deal?'  
            score += 1
            win += 1
            in_play = False 
        dealer_result = 'Dealer - hand value: ' + str(dealer.get_value())    
            
# draw handler    
def draw(canvas):
    canvas.draw_text('B L A C K J A C K', (150, 70), 40, 'Black')	
    text_score = ('Score: ' + str(score) + 
                  ' [win:' + str(win) + ' loss:' + str(loss) + ']')
    canvas.draw_text(text_score, (200, 120), 20, 'Yellow')	
    canvas.draw_text('Player - hand value: ' + str(player.get_value()), 
                     (10, 180), 20, 'White')
    canvas.draw_text(dealer_result, (10, 380), 20, 'White')	
    # message outcome display
    canvas.draw_text(outcome, (20, 570), 20, 'Yellow')
    # draw player & dealer hands
    player.draw(canvas, [10, 200], 'player')
    dealer.draw(canvas, [10, 400], 'dealer')    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
