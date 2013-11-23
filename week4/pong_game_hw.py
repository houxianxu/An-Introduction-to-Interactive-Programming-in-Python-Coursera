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

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel_horizontal = random.randrange(2, 4)
    ball_vel_vertical = random.randrange(1, 3)

    if direction == RIGHT:
    	ball_vel[0] = ball_vel_horizontal
    	ball_vel[1] = -ball_vel_vertical

    if direction == LEFT:
    	ball_vel[0] = -ball_vel_horizontal
    	ball_vel[1] = -ball_vel_vertical



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos, paddle2_pos = HEIGHT/2, HEIGHT/2
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    spawn_ball(LEFT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # collide and bounces off of the top and bottom walls
	if ball_pos[1] <= BALL_RADIUS:
		ball_vel[1] = - ball_vel[1]
	if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
		ball_vel[1] = - ball_vel[1]

	# collide and bounces off of the right and left gutters
	if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
		if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
			ball_vel[0] = -1.1 * ball_vel[0]
			ball_vel[1] = 1.1 * ball_vel[1]
		else:
			score2 += 1
			spawn_ball(RIGHT)

	if ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
		if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
			ball_vel[0] = -1.1 * ball_vel[0]
			ball_vel[1] = 1.1 * ball_vel[1]
		else:
			score1 += 1
			spawn_ball(LEFT)
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < HALF_PAD_HEIGHT:
    	paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
    	paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else: paddle1_pos += paddle1_vel

    if paddle2_pos < HALF_PAD_HEIGHT:
    	paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
    	paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else: paddle2_pos += paddle2_vel

    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")

    # draw scores
    c.draw_text(str(score1), [WIDTH/4, 80], 50, "White")
    c.draw_text(str(score2), [3*WIDTH/4, 80], 50, "White")

        
def keydown(key):
	# set a velocity
	acc_vel = 6
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["w"] == key:
    	paddle1_vel -= acc_vel
    elif simplegui.KEY_MAP["s"] == key:
    	paddle1_vel += acc_vel

    if simplegui.KEY_MAP["up"] == key:
		paddle2_vel -= acc_vel
    elif simplegui.KEY_MAP["down"] == key:
    	paddle2_vel += acc_vel
   
def keyup(key):
	# set the velocity = 0
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["w"] == key:
    	paddle1_vel = 0
    elif simplegui.KEY_MAP["s"] == key:
    	paddle1_vel = 0

    if simplegui.KEY_MAP["up"] == key:
		paddle2_vel = 0
    elif simplegui.KEY_MAP["down"] == key:
    	paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button("Restart", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
