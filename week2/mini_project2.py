# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
guess_range = 100
remain_guess = 7
secret_num = random.randrange(guess_range)


# helper function to start and restart the game
def new_game():
    global guess_range, remain_guess, secret_num
    print "\n"
    print "new game, range is from 0 to ", guess_range-1
    print "remaining guesses is ", remain_guess
    print "\n"


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global guess_range, remain_guess, secret_num
    guess_range = 100
    remain_guess = 7
    secret_num = random.randrange(guess_range)

    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global guess_range, remain_guess, secret_num
    guess_range = 1000
    remain_guess = 10
    secret_num = random.randrange(guess_range)

    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global guess_range, remain_guess, secret_num
    remain_guess -= 1
    guess = float(guess)
    print "Guess is ", guess
    print "the remaining guesses is", remain_guess
    
    if secret_num == guess:
        print "Correct!"
        if guess_range == 100:
            range100()
        elif guess_range == 1000:
            range1000()
    else:
        if secret_num > guess:
            print "Lower!"
        else:
            secret_num < guess
            print "Higher!"
        # whether useing up all the chance to guess
        if remain_guess == 0:
            print "Bad luck, you lose!"
            # restart the game accordingly
            if guess_range == 100:
                range100()
            elif guess_range == 1000:
                range1000()
    
# create frame
frame = simplegui.create_frame("Guessing number", 200, 200)

# register event handlers for control elements
frame.add_button("Range100", range100, 100)
frame.add_button("Range1000", range1000, 100)
frame.add_input("Inut guess", input_guess, 100)


# call new_game and start frame
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
