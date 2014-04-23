# Mini-project: "Stopwatch: The Game"
import simplegui

# globals
WIDTH = 200
HEIGHT = 200
tick_period = 100
time_counter = 0
number_of_draws = 0
success_draws = 0
timer_started = False

# helper functions
def format(time):
    minutes = str(time / (60 * 10))
    seconds = str((time % (60 * 10)) / 10)
    miliseconds = str((time % (60 * 10)) % 10)    
    if len(seconds) < 2:
        seconds = "0" + seconds
    return str(minutes) + ":"  + str(seconds) + "." + str(miliseconds)

def calc_result():    
    return str(success_draws) + "/" + str(number_of_draws)  

# event handlers
def tick():
    global time_counter
    time_counter += 1

def draw(canvas):
    canvas.draw_text(format(time_counter), [WIDTH // 2 - 50, HEIGHT // 2 + 15], 40, "Red")
    result = calc_result()
    font_size = 30
    position_x = WIDTH - 5 - (len(result) * (font_size // 2))
    canvas.draw_text(result, [position_x, 30], font_size, "Green")

def start_timer():
    global number_of_draws, timer_started
    if not timer_started:
        timer.start()
        number_of_draws += 1
        timer_started = True
    
def stop_timer():
    global success_draws, timer_started
    if timer_started:
        timer.stop()
        if (time_counter % (60 * 10)) % 10 == 0:
            success_draws +=1 
        timer_started = False        

def reset_timer():
    global time_counter, success_draws, number_of_draws
    stop_timer()
    time_counter = 0  
    success_draws = 0
    number_of_draws = 0
    
# create frame, buttons & timer and attach event handlers
timer = simplegui.create_timer(tick_period, tick)
frame = simplegui.create_frame("Stopwatch: The Game", WIDTH, HEIGHT)
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)
frame.set_draw_handler(draw)

# Start game
frame.start()