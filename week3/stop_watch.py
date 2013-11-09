# template for "Stopwatch: The Game"
import simplegui
# define global variables
time_increment = 0
exact_stop = 0
total_stop = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    t_A = t % 600
    BC = t_A / 10
    B = BC / 10
    C = BC % 10
    D = t_A % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)


    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global running
    running = True
    timer.start()

def stop_button_handler():
    timer.stop()
    global exact_stop, total_stop, running
    if running:
        total_stop += 1
        if time_increment % 10 == 0:
            exact_stop += 1

    running = False


def reset_button_handler():
    global time_increment, total_stop, running, exact_stop
    timer.stop()
    time_increment, total_stop, exact_stop = 0, 0, 0
    running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_increment
    time_increment += 1
    # print time_increment
    

# define draw handler
def draw_handler(canvas):
    formatted_time = str(format(time_increment))
    formatted_stop = str(exact_stop) + "/" + str(total_stop)
    canvas.draw_text(formatted_time, (120, 110), 30, 'White')
    canvas.draw_text(formatted_stop, (260, 30), 20, 'White')


    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button("Start", start_button_handler)
stop_button = frame.add_button("Stop", stop_button_handler)
reset_button = frame.add_button("Reset", reset_button_handler)



# start frame
frame.start()
# timer.start()
# Please remember to review the grading rubric
