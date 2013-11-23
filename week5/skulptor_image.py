# draggable magnifier on a map

import simplegui

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

# image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scale factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]

#Event handler
# Move magnifier to clicked position
def click(pos):
	global mag_pos
	mag_pos = list(pos)

# Draw map and magnifier region
def draw(canvas):
	# Draw map
	canvas.draw_image(image, 
				[MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT],
				[CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_HEIGHT, CAN_HEIGHT])

	# Draw magnifier
	map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
	map_rectangle = [MAG_SIZE, MAG_SIZE]
	mag_center = mag_pos
	mag_rectangle = [MAG_SIZE, MAG_SIZE]
	canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)

# Create frame
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# Start frame
frame.start()



