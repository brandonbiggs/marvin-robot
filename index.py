#!/usr/bin/env python3
######################################################
# Brandon Biggs
# Examples of some of the fun things that your Mindstorm can do
# Marvin is the Gripp3r and Optimus is the Ev3rstorm
######################################################

from modules.robot import Marvin
from modules.robot import Optimus

marvin = Marvin()

marvin.print_to_screen("Print test to screen!")
marvin.speak("Hello. I am Marvin. Nice to meet you!")
marvin.close_hands()
marvin.open_hands()
marvin.move_forward()
marvin.move_backward()
marvin.turn("right")
marvin.turn("left")

optimus = Optimus()
optimus.print_to_screen("Print to screen!")
optimus.speak("Hello. I am Optimus. Nice to meet you.")
optimus.move_forward()
optimus.move_backward()
optimus.turn("right")
optimus.turn("left")
