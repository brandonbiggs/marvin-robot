#!/usr/bin/env python3
######################################################
# Here you will find some examples of code that the Lego Mindstorm can run.
# Inside of the parenthesis, you'll find multiple parameters of "word=".
#       These are all examples of things that you can use, but don't have to.
#       If you want to use these, just change the number or text inside of parenthesis
######################################################

from modules.robot import *

robot = Robot()
robot.print_to_screen(statement="Print test to screen!")
robot.speak(statement="Hello. I am Marvin. Nice to meet you!")
robot.move_backward(seconds_to_move=3, speed=5)
robot.move_forward(seconds_to_move=3, speed=5)
robot.wait(seconds=5)

gripper = Gripper()
gripper.turn("right", degrees=90, seconds=1, speed=6)
gripper.turn("left", degrees=90, seconds=1, speed=6)
gripper.close_hands()
gripper.open_hands()

everstorm = Everstorm()
everstorm.turn("right", degrees=90, seconds=1, speed=6)
everstorm.turn("left", degrees=90, seconds=1, speed=6)