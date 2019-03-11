#!/usr/bin/env python3
######################################################
# Brandon Biggs
# Unit test the robot functionality
######################################################

from modules.robot import *
robot = Robot(debug=False)

robot.print_to_screen()
robot.print_to_screen("Test statement")
robot.print_to_screen(5)

robot.speak()
robot.speak("I am speaking! I'm about to wait for 5 seconds")

robot.wait(5)

robot.set_speaker_volume(100)

robot.beep(5, override=True)

# print("UNIT TEST: MOVE FORWARD.")
# print("NOT YET WRITTEN.")
#
# print("UNIT TEST: MOVE BACKWARD.")
# print("NOT YET WRITTEN.")
#
# print("UNIT TEST: TURN")
# print("NOT YET WRITTEN.")


robot.set_button_colors(color="yellow", button="left", brightness=100)
robot.set_button_colors(color="black", button="BLARG")

##########################################
# Test the play random song functionality
robot.sing_random_song()
robot.sing_random_song("blarg")
robot.sing_random_song("long")

##########################################
# Test the play tone functionality
# print("UNIT TEST: PLAY TONE")
robot.play_random_tone()
robot.play_random_tone("short")
robot.play_random_tone("long")
robot.play_random_tone("blarg")

# print("UNIT TEST: GRIPP3R")
# print("NOT YET WRITTEN.")
#
# print("UNIT TEST: EV3RSTORM")
# print("NOT YET WRITTEN.")
