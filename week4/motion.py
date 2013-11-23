import simplegui

# Initializes globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [3, 4] # pixels per tick
time = 0

# define event handlers
def tick():
	global time
	time += 1

def draw(canvas):
	# creat a list to hold ball position
	ball_pos = [0, 0]

	# calculate ball position
	ball_pos[0] = init_pos[0] + time * vel[0]
	ball_pos[1] = init_pos[1] + time * vel[1]

	# draw the ball
	canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()

# instead of using timer, we can change ball_pos directly
# the draw handler runs every 60 times of a second.
# def draw(canvas):
# 	ball_pos[0] += vel[0]
# 	ball_pos[1] += vel[1]
# 	canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White") 