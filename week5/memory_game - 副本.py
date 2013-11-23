# this code is from other's which I think is very nice!
# http://www.codeskulptor.org/#user24_1NAIJmdxLwwMAiq.py



debug=False # Changing to True will remove blinds and print stuff

# Implementation of card game - Memory. 

# Elected to make it scalable, so you
# can dynamically change the board layout
# this required writing everying positional 
# in relative terms.

import simplegui
import random
import time

# Number of row and columns, and turn counter
# Note that rows*columns must be even
columns=4   # i.e., the game width
rows=4      # i.e., the game height 
turns=0     # turn counter
won=0       # has user won the game? I use this 
            # flag to index into colour lists
            # for flare when user has won.
view_time=1.5   # how long, in seconds, before auto-hide flipped.
solved_time=0.7 # how long before solved pair is hidden.
        
images=False    # This bool determines if images are drawn
                # Scroll to bottom: images are loaded into a list.
                # Images are a handful of my son's toy cars
                # although I did consider taking screen shots
                # of all of Scott's ties ;)
    
# Tile Dimensions
c=20 # Could impliment function to dynamically modify tiles...lazy
HEIGHT=100+c
WIDTH=90+c

# Calculated constants
TILES=rows*columns  # The area of play
CARDS=TILES/2       # The number of unique items

# helper functions

def frame_setup():
    '''
    Set up the frame parameters.
    Shout out to other student for idea of farming this to function,
    and for dynamic resizing ideas: 
        http://www.codeskulptor.org/#user23_JnBUJ560XA_43.py
    '''
    global frame,label,inp,img_toggle
    frame.add_button("Restart", new_game)   
  
    if images==True: img_flag="ON]"
    else: img_flag="OFF]"      
    img_toggle=frame.add_button("Toggle Images [currently " +\
                     img_flag, img_mode)

    frame.add_label("") # add a spacer blank line
    
    inp = frame.add_input('Change the Board! Enter new "width,height" (e.g., "8,2"):', resize, 100)
    
    frame.add_label("") # add a spacer blank line
    
    label = frame.add_label("Turns = 0")
    label2 = frame.add_label("Unique objects = " +\
                             str(CARDS))
    
    # register event handlers
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)

def resize(text_input):
    '''
    check user input (+int, +int), if good, update variables and restart frame
    '''
    # frame has to be global or you can't stop existing one.
    global frame, columns, rows, TILES, CARDS

    # style choice: immediatley clear input box
    inp.set_text('')

    #reusable error msg.    
    msg="Invalid input, please try again. "

    # split the text at comma
    text_input = text_input.split(',')
    
    # make sure only two comma seperated 'things' entered
    # break out of this function with a return if error.
    # Note that 'None' is the default return and exists in
    # all functions even if you don't explicitly return.
    if len(text_input)!=2:
        print msg
        return     
    
    # make sure the thigns are numbers by trying to type them to ints
    try:
        val=int(text_input[0])
    except ValueError:
        print msg
        return
    try:
        val=int(text_input[1])
    except ValueError:
        print msg
        return
    
    # assign said ints to variables for brevity
    c=int(text_input[0])
    r=int(text_input[1])
    
    # check that they're non-negative, non-zero, 
    # and there are sufficient images loaded to run
    # at given size if in image mode
    # shouldn't constrain if in text mode, but...I'm lazy.
    if c<=0 or r <= 0 or c*r%2!=0:
        print msg
        return
    
    if (c*r)/2>len(toy_img_urls):
        print msg + "Sorry, insufficient images for a board of that size."
        return
    
    # if user input passed the above tests and 
    # execution wasn't returned out of this function
    # then use the input to update variables and then
    # stop the existing frame and start another.
    columns=c
    rows=r
    TILES=rows*columns
    CARDS=TILES/2
    frame.stop()
    frame = simplegui.create_frame("Memory", WIDTH*columns, HEIGHT*rows)
    frame_setup()
    new_game()
    frame.start()    

def img_mode():
    # just toggles image mode and updates label
    global images
    images=not images

    if images==True: img_flag="ON]"
    else: img_flag="OFF]"
        
    img_toggle.set_text("Toggle Images [currently " + img_flag)
    
def new_game():
    global deck,turns,won, img_dict
    turns,won = 0,0
    label.set_text("Turns = 0")
    
    # make a randomized 'deck'
    deck=2*[n for n in range(CARDS)]
    random.shuffle(deck)
    
    # decided to handle all game logic in one list
    # with the value followed by a flag that is
    # 0 if hidden, 1 if exposed, and 2 if solved
    # (later added third spot for timestamp)
    deck = [[n,0,0] for n in deck[:]]
    # e.g., [[0, 0, 0], [3, 0, 0],...]
    
    # for images, program makes a randomized dictionary
    # with key=card (int) and value=image object

    random.shuffle(toy_img_objects) 
    img_dict={} # new empty dictionary
    for card in range(CARDS):
        img_dict[card]=toy_img_objects[card]
    
def take_turn():
    # just updates turns
    global turns
    turns+=1
    label.set_text("Turns = " + str(turns))

    
# MOUSE MOUSE MOUSE MOUSE DO STUFF    
    
# define event handlers
def mouseclick(pos):
    global deck, turns, won
    
    # Use the position to determine pick
    # i.e., PICK is simply the index into the deck list(!)
    pick=(pos[0]/WIDTH)+columns*(pos[1]/HEIGHT)
    if debug: print "pick: "+str(pick)

    # create a list of exposed cards, as [value, index] pairs.
    exposed=[[n,deck.index([n,flag,t])] for n,flag,t in deck if flag==1]
 
    # if nothing is flipped, flip what is clicked on (if valid)  
    if len(exposed)==0:
        if deck[pick][1]==0:
            deck[pick][1]=1

    # if one is flipped...        
    if len(exposed)==1:
        # ...and you find a match (same value, different deck index)
        if deck[pick][0]==exposed[0][0] and pick!=exposed[0][1]:
            take_turn()
            deck[pick][1], deck[exposed[0][1]][1]=2,2
            timestamp=time.time()
            deck[pick][2], deck[exposed[0][1]][2]=timestamp,timestamp
        # ...and you do NOT find a match
        if deck[pick][1]==0:
            take_turn()
            deck[pick][1]=1
            timestamp=time.time()
            deck[pick][2], deck[exposed[0][1]][2]=timestamp,timestamp
    # if two are already flipped...
    if len(exposed)==2:
        if deck[pick][1]==0: #...and you click on a valid option
            deck[exposed[0][1]][1],deck[exposed[1][1]][1]=0,0 # ...hide the previously flipped...
            deck[exposed[0][1]][2],deck[exposed[1][1]][2]=0,0
            deck[pick][1]=1 #...and flip the selected
    
    # determine if the game has been won
    if len([flag for n,flag in deck if flag==2])==TILES and won==0:
        won=1
        exclamations=["By the spotted tie of Rixner,","Hot pot of coffee,", "By the beard of Zeus,", "Son of a bee-sting,", "Uncle Jonathan's corn-cob pipe,", "Knights of Columbus,", "Sweet grandmother's spatula,", "Oh, Saint Damien's beard,", "Sweet Lincoln's mullet,", "Great Odin's Raven,", "By the Hammer of Thor,"]  
        print random.choice(exclamations) + \
                "\nyou won in " + str(turns) + \
                " turns for " + str(CARDS) + " objects!\n"

                
# DRAW DRAW DRAW DRAW STUFF                
                
def draw(canvas):
    # draw SOLVED BACKGROUND as vertical lines of width = WIDTH
    # change colour if user wins (using won flag as index into list)
    colour=["#505050","#263F7D"][won]
    global deck # for hiding tiles based on time
    for line in range(TILES):
        if deck[line][1]==2:
            canvas.draw_line([(WIDTH/2)+(line%columns)*WIDTH,0+line/columns*HEIGHT],\
                             [(WIDTH/2)+(line%columns)*WIDTH,HEIGHT+line/columns*HEIGHT],WIDTH,\
                             colour)
            
    # CARDS AS TEXT
    # draw values as text, uses a counter to index through
    # n[0]=value, n[1]=0,1,or2, n[3]=0 or timestamp
    if not images:
        i = 0
        for n in deck:
            if n[1]==1 and n[2]!=0:
                if time.time()-n[2]>view_time:
                    n[1],n[2]=0,0
            if n[1]==1 or debug or won or (n[1]==2 and time.time()-n[2]<solved_time):
                # get width of number and use to centre it
                text_width=frame.get_canvas_textwidth(str(n[0]),.75*HEIGHT)
                start=(WIDTH-text_width)//2
                canvas.draw_text(str(n[0]),[start+i%(WIDTH*columns),\
                        (.75*HEIGHT)+i/(WIDTH*columns)*HEIGHT],.75*HEIGHT,"White") 
            i+=WIDTH

    # CARDS AS IMAGES        
    # draw images if desired
    if images:
        i = 0
        for n in deck:
            # for every card, if it is showing or we're debugging:
            if n[1]==1 and n[2]!=0:
                if time.time()-n[2]>view_time:
                    n[1],n[2]=0,0
            if n[1]==1 or debug or won or (n[1]==2 and time.time()-n[2]<solved_time):
                canvas.draw_image(img_dict[n[0]],\
                                  [144, 160],\
                                  [287,319],\
                                  [.5*WIDTH+i%(WIDTH*columns),\
                                   (.5*HEIGHT)+i/(WIDTH*columns)*HEIGHT],\
                                  [WIDTH,HEIGHT])
            i+=WIDTH    
    
    
    # draw BLINDS, exactly the same as solved background (i.e., lines),
    # but on top of numbers/images
    for line in range(TILES):
        if deck[line][1]==0 and not debug:
            canvas.draw_line([(WIDTH/2)+(line%columns)*WIDTH,0+line/columns*HEIGHT],\
                             [(WIDTH/2)+(line%columns)*WIDTH,HEIGHT+line/columns*HEIGHT],WIDTH,\
                             "DarkOliveGreen")
            
    # draw the fenceposts (make the grid)
    colour=["#FFA500","#5F9EA0"][won]
    # --vertical
    for line in range(1,columns):
        canvas.draw_line([line*WIDTH,0],[line*WIDTH,rows*HEIGHT],2,colour)
    # --horizontal
    for line in range(1,rows):
        canvas.draw_line([0,line*HEIGHT],[columns*WIDTH, line*HEIGHT],2,colour)
    # --outline
    canvas.draw_polygon([[0,0],[0,HEIGHT*rows],\
                         [WIDTH*columns,HEIGHT*rows],\
                         [WIDTH*columns,0]],2,colour)

    # reward "WIN!", with drop shadow (ohh, ahh)
    if won==1:
        text_width=frame.get_canvas_textwidth("WIN!",.5*HEIGHT)
        start=(WIDTH*columns-text_width)//2
        canvas.draw_text("WIN!",[start+4,(.5*HEIGHT*rows+.15*HEIGHT)+4],.5*HEIGHT,"Black")
        canvas.draw_text("WIN!",[start,.5*HEIGHT*rows+.15*HEIGHT],.5*HEIGHT,"#00FF00")   
       
# get the images ready (load them right away into a list of img objects)
toy_img_urls=['http://i.imgur.com/GlfVXzD.jpg',\
              'http://i.imgur.com/JQygurL.jpg',\
              'http://i.imgur.com/8xb40KR.jpg',\
              'http://i.imgur.com/ww1yaSG.jpg',\
              'http://i.imgur.com/oa47QEP.jpg',\
              'http://i.imgur.com/rZ8Ypnx.jpg',\
              'http://i.imgur.com/9AXU123.jpg',\
              'http://i.imgur.com/Sjuakpi.jpg',\
              'http://i.imgur.com/Ytaz2lz.jpg',\
              'http://i.imgur.com/6qNIboJ.jpg',\
              'http://i.imgur.com/UAfJ67P.jpg',\
              'http://i.imgur.com/R1SLVzu.jpg',\
              'http://i.imgur.com/fTyA0bG.jpg',\
              'http://i.imgur.com/6iyr6Xc.jpg',\
              'http://i.imgur.com/WCCkHjc.jpg',\
              'http://i.imgur.com/NJQzB5k.jpg',\
              'http://i.imgur.com/00H8RWK.jpg',\
              'http://i.imgur.com/ytiD1XX.jpg',\
              'http://i.imgur.com/AlmDX71.jpg',\
              'http://i.imgur.com/t4LcBO1.jpg',\
              'http://i.imgur.com/18Qd1Wc.jpg',\
              'http://i.imgur.com/oP5u0gL.jpg',\
              'http://i.imgur.com/BsGGFfW.jpg',\
              'http://i.imgur.com/kv7sFrr.jpg',\
              'http://i.imgur.com/zZ8NpBz.jpg',\
              'http://i.imgur.com/ONCMkUd.jpg',\
              'http://i.imgur.com/u4Pjd7W.jpg',\
              'http://i.imgur.com/3eINxHd.jpg',\
              'http://i.imgur.com/drViTDY.jpg',\
              'http://i.imgur.com/twjYtIy.jpg',\
              'http://i.imgur.com/flgDeDe.jpg',\
              'http://i.imgur.com/hNIJRwK.jpg',\
              'http://i.imgur.com/2t2IFRM.jpg',\
              'http://i.imgur.com/FnnDgil.jpg',\
              'http://i.imgur.com/FCzhq8r.jpg',\
              'http://i.imgur.com/Gl6xFro.jpg',\
              'http://i.imgur.com/6c2Gcb0.jpg',\
              'http://i.imgur.com/rGHyxKB.jpg',\
              'http://i.imgur.com/KAVZjGN.jpg',\
              'http://i.imgur.com/MwRELeZ.jpg',\
              'http://i.imgur.com/XxIpKIx.jpg',\
              'http://i.imgur.com/VhFNdb8.jpg']
toy_img_objects=[simplegui.load_image(url) for url in toy_img_urls]    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH*columns, HEIGHT*rows)
frame_setup()

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric