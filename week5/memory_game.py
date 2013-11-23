# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards_dec, exposed, DELTA, state, unpair_index_state1, unpair_index_state2, count, paired
    cards_dec = range(8) + range(8)
    random.shuffle(cards_dec)
    state = 0
    unpair_index_state1 = None
    unpair_index_state2 = []
    count = 0
    label.set_text("Turns = " + str(count))
    paired = [False] * 16
    print paired
    print cards_dec
    exposed = [False] * 16
    DELTA = 800.0 / 16 / 2

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, card_index_1, card_index_2, count, paired
    x, y = pos[0], pos[1]
    if (y > 0 and y < 100) and (x < 800 and x > 0):
        i = int (x / (DELTA * 2))
        exposed[i] = True
        if state == 0:
            card_index_1 = i
            state = 1
            count += 1

        elif state == 1 and i != card_index_1:
                card_index_2 = i

                if cards_dec[card_index_1] == cards_dec[card_index_2]:
                    state = 0
                else:
                    state = 2

        elif card_index_1 != i and card_index_2 != i and state == 2:
            count += 1

            if not paired[card_index_1]:
                exposed[card_index_1] = False
                card_index_1 = i
                state = 1
            if not paired[card_index_2]:
                exposed[card_index_2] = False
                card_index_1 = i
                state = 1
            
            if (cards_dec[card_index_1] == cards_dec[i]) and card_index_1 != i:
                paired[i], paired[card_index_1] = True, True
                card_index_1 = i
                card_index_2 = None
                state = 1
            elif (cards_dec[card_index_2] == cards_dec[i]) and card_index_2 != i:
                paired[i], paired[card_index_2] = True, True
                card_index_2 = None
                state = 1
            else:
                card_index_1 = i
                card_index_2 = None
 


        label.set_text("Turns = " + str(count))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards_dec, exposed, DELTA
    ini_pos = DELTA
    for i in xrange(16):
        if exposed[i]:
            canvas.draw_text(str(cards_dec[i]), (ini_pos-10, 60), 40, "White")
        else:
            canvas.draw_polygon([(ini_pos-DELTA, 0), (ini_pos-DELTA, 100),(ini_pos+ DELTA, 100), (ini_pos+ DELTA, 0) ], 1, 'Red', 'Green')

        ini_pos += 2 * DELTA
     

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric  