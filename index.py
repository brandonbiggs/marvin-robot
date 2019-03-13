#!/usr/bin/env python3
######################################################
# Here you will find some examples of code that the Lego Mindstorm can run.
# Inside of the parenthesis, you'll find multiple parameters of "word=".
#       These are all examples of things that you can use, but don't have to.
#       If you want to use these, just change the number or text inside of parenthesis.

# To see more information about each function, type
# print(robot.<name of function without parenthesis>.__doc__)
# Example - print(robot.beep.__doc__)
######################################################

from modules.robot import *

robot = Robot()

# Print to the robots screen
robot.print_to_screen(statement="Print test to screen!")

# Move the robot
robot.move_forward(distance_in_feet=1.0)
robot.move_backward(distance_in_feet=1.0)
robot.turn(direction="right")
robot.turn(direction="left")

# Make the robot produce noise
robot.set_speaker_volume(100)
robot.speak(statement="Hello. I am a robot. Nice to meet you!")
robot.beep(5)
robot.sing_random_song()

# Make the robot's buttons change color
robot.set_button_colors(color="yellow", button="left", brightness=100)

robot.wait(seconds=5)

# Gripper can run all of the same commands as robot + the following commands
gripper = Gripper()
gripper.close_hands()
gripper.open_hands()

# Everstorm can run all of the same commands as robot.
everstorm = Everstorm()
