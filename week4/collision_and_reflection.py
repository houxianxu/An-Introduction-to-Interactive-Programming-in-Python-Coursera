import simplegui

# Initializes globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-5, 0.5] # pixels per tick

# define event handlers
def draw(canvas):
 	ball_pos[0] += vel[0]
	ball_pos[1] += vel[1]

	# collide and reflect
	if ball_pos[0] <= BALL_RADIUS:
		vel[0] = - vel[0]
	if ball_pos[0] >= WIDTH - 1 - BALL_RADIUS:
		vel[0] = - vel[0]

	# draw the ball
	canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
