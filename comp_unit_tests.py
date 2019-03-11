#!/usr/bin/env python3
######################################################
# Brandon Biggs
# Unit testing everything - First time writing this. May need more work.
# This sets the robot to debug, so this won't run on robot. Meant to run on the
# computer of the person to test each function. Will need to write one of these for
# the robot.
######################################################

from modules.robot import *

robot = Robot(debug=True)

print("\n\nUNIT TEST: PRINT_TO_SCREEN.")
robot.print_to_screen()
robot.print_to_screen(12)
robot.print_to_screen(-1)
robot.print_to_screen("Test statement")

print("\n\nUNIT TEST: SPEAK.")
robot.speak()
robot.speak(12)
robot.speak(-12)
robot.speak("test statement!")

print("\n\nUNIT TEST: WAIT.")
robot.wait()
robot.wait("test")
robot.wait(10)
robot.wait(-1)

print("\n\nUNIT TEST: BEEP")
robot.beep()
robot.beep(5)
robot.beep(-5)
robot.beep(100000)
robot.beep("5")
robot.beep("five")
robot.beep(300, override=True)

print("\n\nUNIT TEST: SET VOLUME")
robot.set_speaker_volume()
robot.set_speaker_volume(100)
robot.set_speaker_volume(0)
robot.set_speaker_volume(-1)
robot.set_speaker_volume(9001)
robot.set_speaker_volume("one")

print("\n\nUNIT TEST: MOVE FORWARD.")
print("NOT YET WRITTEN.")

print("UNIT TEST: MOVE BACKWARD.")
print("NOT YET WRITTEN.")

print("UNIT TEST: TURN")
print("NOT YET WRITTEN.")

##########################################
# Test the setting colors of the buttons functionality
print("\n\nUNIT TEST: SET BUTTON COLORS")
robot.set_button_colors()
robot.set_button_colors(color="green", button="left", brightness=10)
robot.set_button_colors(color="green", button="right")
robot.set_button_colors(color="black", button="right")
robot.set_button_colors(color="orange", button="left")
robot.set_button_colors(color="yellow", button="right")
robot.set_button_colors(color="amber", button="left")
robot.set_button_colors(color="red", button="right")
robot.set_button_colors(color="amber", button="left", brightness=-100)
robot.set_button_colors(color="red", button="right", brightness=10000)

print("\n\nFOLLOWING SHOULD ERROR.")
robot.set_button_colors(color="black", button="BLARG")
robot.set_button_colors(color="BLARG", button="right")
robot.set_button_colors(color=12, button="right")
robot.set_button_colors(color="black", button=12)
robot.set_button_colors(color="blue", button="right")

##########################################
# Test the play random song functionality
print("\n\nUNIT TEST: SING RANDOM SONG.")
robot.sing_random_song()
robot.sing_random_song("short")
robot.sing_random_song("long")
robot.sing_random_song("blarg")
robot.sing_random_song(12)
robot.sing_random_song(-12)

##########################################
# Test the play tone functionality
print("\n\nUNIT TEST: PLAY TONE")
robot.play_random_tone()
robot.play_random_tone("short")
robot.play_random_tone("long")
robot.play_random_tone("blarg")
robot.play_random_tone(12)
robot.play_random_tone(-12)

print("\n\nUNIT TEST: GRIPP3R")
print("NOT YET WRITTEN.")

print("\n\nUNIT TEST: EV3RSTORM")
print("NOT YET WRITTEN.")
