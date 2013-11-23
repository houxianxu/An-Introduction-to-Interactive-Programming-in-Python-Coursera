import simplegui

# Initializes globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
	canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
	delta = 4
	if key == simplegui.KEY_MAP["left"]:
		ball_pos[0] -= delta
	elif key == simplegui.KEY_MAP["right"]:
		ball_pos[0] += delta
	elif key == simplegui.KEY_MAP["up"]:
		ball_pos[1] -= delta
	elif key == simplegui.KEY_MAP["down"]:
		ball_pos[1] += delta

# create frame
frame = simplegui.create_frame("Position ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()

