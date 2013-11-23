import simplegui

# Initializes globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0] 

# define event handlers
def draw(canvas):
 	ball_pos[0] += vel[0]
	ball_pos[1] += vel[1]
	# draw the ball
	canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
	delta = 1
	if key == simplegui.KEY_MAP["left"]:
		vel[0] -= delta
	elif key == simplegui.KEY_MAP["right"]:
		vel[0] += delta
	elif key == simplegui.KEY_MAP["up"]:
		vel[1] -= delta
	elif key == simplegui.KEY_MAP["down"]:
		vel[1] += delta

	print ball_pos, vel


# create frame
frame = simplegui.create_frame("Ball motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
