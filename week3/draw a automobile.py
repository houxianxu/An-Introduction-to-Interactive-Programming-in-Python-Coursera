# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = []
iteration = 0
max_iterations = 10

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    """???  Part of mystery computation."""
    return 0.5 * (current + n / current)

# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result
    
    # Stop iterating after max_iterations
    if iteration == 1:
        timer.stop()
        print "Output is", max(result)
    else:
        if iteration % 2 == 0:
        	iteration / 2
        else iteration * 3 + 1
    result.append(iteration)
# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(13)
timer.start()