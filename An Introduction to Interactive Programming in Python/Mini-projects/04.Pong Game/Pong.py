# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
VERTICAL = False
HORIZONTAL = True
HITS = 0

# Helper functions
def paddle_init(paddle):
    """ Initialize the paddle when game starts """
    global paddle1_vel, paddle2_vel
    if paddle == RIGHT:	# player Two paddle (right)
        x1 = WIDTH - PAD_WIDTH
        x2 = WIDTH
        paddle2_vel = 0
    else:				# player One paddle (left)
        x1 = 0
        x2 = PAD_WIDTH
        paddle1_vel = 0
    y1 = HEIGHT / 2 - HALF_PAD_HEIGHT
    y2 = HEIGHT / 2 + HALF_PAD_HEIGHT
    return [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]

def paddle_change_pos(pos, vel):
    """ Change the position of paddle according to current velocity """
    y1 = pos[0][1] + vel
    y2 = pos[2][1] + vel
    return [[pos[0][0], y1], [pos[1][0], y1], [pos[2][0], y2], [pos[3][0], y2]]

def ball_generate_velocity(direction):
    """ Generates initial ball velocity """
    x_comp = random.randrange(120,240) / 60.0
    y_comp = -(random.randrange(60,180)  / 60.0)
    if direction != RIGHT:
        x_comp = -x_comp
    return [x_comp, y_comp]    

def ball_increase_velocity():
    """ Increases the ball velocity with 10% after hit with paddle """
    global ball_vel
    ball_vel[0] = ball_vel[0] * 1.10
    ball_vel[1] = ball_vel[1] * 1.10    

def ball_bounce(wall):
    """ Bouncing ball from walls (paddles) depending it is vertical or horizontal ones """
    if wall: # top & bottom walls
        ball_vel[1] = -ball_vel[1]
    else:    # left or right walls
        ball_vel[0] = -ball_vel[0]    

def spawn_ball(direction):
    """ Initialize ball_pos and ball_vel for new bal in middle of table """
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = ball_generate_velocity(direction) # Ball velocity randomization 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, score1, score2  
    score1 = 0
    score2 = 0
    paddle1_pos = paddle_init(LEFT)
    paddle2_pos = paddle_init(RIGHT)
    direction = bool(random.randrange(0,2)) # randomly selects Left(0) or right(1) direction
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    start = 0
    while start < HEIGHT:
        canvas.draw_line([WIDTH / 2, start],[WIDTH / 2, start + 12], 1, "White")
        start += 24
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ((ball_vel[1] < 0 and ball_pos[1] - BALL_RADIUS <= 0) or 
        (ball_vel[1] > 0 and ball_pos[1] + BALL_RADIUS >= HEIGHT)):
            ball_bounce(HORIZONTAL) # checks for touch with ceiling or bottom walls

    if ball_vel[0] < 0 and ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if paddle1_pos[1][1] <= ball_pos[1] and paddle1_pos[2][1]>= ball_pos[1]:
            ball_bounce(VERTICAL)		# checks for touch with left gutter or paddle
            ball_increase_velocity()  	# increase speed by 10%
        else:  
            spawn_ball(RIGHT)			# player one (left) misseed the ball
            score2 += 1					# point for player two
    elif ball_vel[0] > 0 and ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if paddle2_pos[1][1] <= ball_pos[1] and paddle2_pos[2][1]>= ball_pos[1]:
            ball_bounce(VERTICAL)		# checks for touch with left gutter or paddle
            ball_increase_velocity() 	# increase speed by 10%
        else:  
            spawn_ball(LEFT)			# player two (right) misseed the ball
            score1 += 1					# point for player one
    else:        
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_vel < 0 and paddle1_pos[0][1] >= 0 or 
        paddle1_vel > 0 and paddle1_pos[2][1] <= HEIGHT):
            paddle1_pos = paddle_change_pos(paddle1_pos, paddle1_vel) 
    if (paddle2_vel < 0 and paddle2_pos[0][1] >= 0 or 
        paddle2_vel > 0 and paddle2_pos[2][1] <= HEIGHT):
            paddle2_pos = paddle_change_pos(paddle2_pos, paddle2_vel)    
        
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 1, 'Green', 'Green')
    canvas.draw_polygon(paddle2_pos, 1, 'Red', 'Red')
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4 - 20, 100), 60, 'Green')
    canvas.draw_text(str(score2), (WIDTH - WIDTH / 4 - 20, 100), 60, 'Red')
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    move = 4
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -move            
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = move
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -move
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = move
         
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button = frame.add_button('Restart', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
