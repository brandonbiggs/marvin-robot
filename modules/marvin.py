#!/usr/bin/env python3
######################################################
# Brandon Biggs
# This is where the magic happens
######################################################
# Marvin Framework/Wrapper

import os
import sys
import time
import ev3dev.ev3 as ev3

class Robot:
    _left_track = "outB"
    _right_track = "outC"
    _on = True
    _off = False

    def __init__(self, left_track="outB", right_track="outC"):
        self._left_track = left_track
        self._right_track = right_track

    @staticmethod
    def _reset_console():
        # '''Resets the console to the default state'''
        print('\x1Bc', end="")

    @staticmethod
    def _set_cursor(state):
        # Turn the cursor on or off on the screen
        if state:
            print('\x1B[?25h', end='')
        else:
            print('\x1B[?25l', end='')

    @staticmethod
    def _set_font(name):
        # Sets the console font
        # A full list of fonts can be found with `ls /usr/share/consolefonts`
        os.system('setfont ' + name)

    # Prints to Marvin's screen
    def print_to_screen(self, statement):
        # sets up the console
        self._reset_console()
        self._set_cursor(self._off)
        self._set_font('Lat15-Terminus24x12')

        # print something to the screen of the device
        print(statement)

        # Sleeps the terminal
        time.sleep(5)

    # Marvin will speak to you
    @staticmethod
    def speak(statement):
        ev3.Sound.speak(statement).wait()

    # Moves the left track
    def move_left_track(self, time_to_move, speed, sleep=True):
        self._move_track(time_to_move, speed, self._left_track, sleep)

    # Moves the right Track
    def move_right_track(self, time_to_move, speed, sleep=True):
        self._move_track(time_to_move, speed, self._right_track, sleep)

    # Moves Marvin forward
    def move_forward(self, time_to_move=3, speed=5):
        self.move_right_track(time_to_move, speed, False)
        self.move_left_track(time_to_move, speed, False)
        time.sleep(time_to_move)

    # Moves Marvin backward
    def move_backward(self, time_to_move=3, speed=5):
        speed = speed * (-1)
        self.move_right_track(time_to_move, speed, False)
        self.move_left_track(time_to_move, speed, False)
        time.sleep(time_to_move)

    @staticmethod
    def _move_track(time_to_move, speed, track, sleep=True):
        movement_time = time_to_move*1000
        movement_speed = speed*100
        motor = ev3.Motor(track)
        motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        if sleep:
            time.sleep(time_to_move)

    @staticmethod
    def wait(seconds=5):
        time.sleep(seconds)

    # TODO - Currently just for 90 degree turns left or right
    def turn(self, degrees, direction):
        if direction == "left":
            self._move_track(1.2, 5, self._left_track)
        elif direction == "right":
            self._move_track(0.9, 5, self._right_track)
        else:
            self.speak("I don't know what direction " + direction + " is. Sorry.")


# Added a unique class for the Ev3rstorm Mindstorm. Inherits from Robot class
class Optimus(Robot):

    def __init__(self):
        Robot.__init__(self)

# Added a unique class for the Gripp3r Mindstorm. Inherits from the Robot Class
class Marvin(Robot):
    # Constants
    _gripper_motor = "outA"

    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        Robot.__init__(self, left_track, right_track)
        self._gripper_motor = gripper_motor
        # self._left_track = left_track
        # self._right_track = right_track

    # Opens Grippers
    def open_hands(self):
        time_to_run = 3000
        speed = -800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run/1000 + 1)

    # Closes Grippers
    def close_hands(self):
        time_to_run = 3000
        speed = 800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run/1000 + 1)

    # TODO - Not yet ready to be implemented.
    @staticmethod
    def shoot_ball():
        print("Not yet defined!")