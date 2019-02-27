#!/usr/bin/env python3
######################################################
# Here you will find some examples of code that the Lego Mindstorm can run.
# Inside of the parenthesis, you'll find multiple parameters of "word=".
#       These are all examples of things that you can use, but don't have to.
#       If you want to use these, just change the number or text inside of parenthesis
######################################################

from modules.robot import *

marvin = Robot()
marvin.print_to_screen(statement="Print test to screen!")
marvin.speak(statement="Hello. I am Marvin. Nice to meet you!")
marvin.move_backward(seconds_to_move=3, speed=5)
marvin.move_forward(seconds_to_move=3, speed=5)
marvin.wait(seconds=5)

marvin = Marvin()
marvin.turn("right", degrees=90, seconds=1, speed=6)
marvin.turn("left", degrees=90, seconds=1, speed=6)
marvin.close_hands()
marvin.open_hands()

optimus = Optimus()
optimus.turn("right", degrees=90, seconds=1, speed=6)
optimus.turn("left", degrees=90, seconds=1, speed=6)