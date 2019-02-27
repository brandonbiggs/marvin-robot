#!/usr/bin/env python3
######################################################
# Brandon Biggs
# This is where the magic happens
######################################################
# Marvin Framework/Wrapper

import os
import sys
import time

try:
    import ev3dev.ev3 as ev3
except ImportError:
    print("Can't find ev3dev package")

# Base class for controlling the Mindstorms
class Robot:
    _left_track = "outB"
    _right_track = "outC"
    _on = True
    _off = False

    def __init__(self, left_track="outB", right_track="outC"):
        self._left_track = left_track
        self._right_track = right_track

    @staticmethod
    def __reset_console():
        # '''Resets the console to the default state'''
        print('\x1Bc', end="")

    @staticmethod
    def __set_cursor(state):
        # Turn the cursor on or off on the screen
        if state:
            print('\x1B[?25h', end='')
        else:
            print('\x1B[?25l', end='')

    @staticmethod
    def __set_font(name):
        # Sets the console font
        # A full list of fonts can be found with `ls /usr/share/consolefonts`
        os.system('setfont ' + name)

    # Moves the left track
    def __move_left_track(self, time_to_move, speed, sleep=True):
        self.__move_track(time_to_move, speed, self._left_track, sleep)

    # Moves the right Track
    def __move_right_track(self, time_to_move, speed, sleep=True):
        self.__move_track(time_to_move, speed, self._right_track, sleep)

    @staticmethod
    def __move_track(time_to_move, speed, track, sleep=True):
        movement_time = time_to_move*1000
        movement_speed = speed*100
        motor = ev3.Motor(track)
        motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        if sleep:
            time.sleep(time_to_move)

    # TODO - Currently just for 90 degree turns left or right. Create formula for turning more than 90 degrees with marvin
    # Turning is tricky as it's different per robot. I've calculated the turning factor for Optimus
    def _turn(self, direction, speed, seconds):
        # To turn left, you have to move the right track forward
        if direction == "left":
            self.__move_right_track(seconds, speed)
        # To turn right, you have to move the left track forward
        elif direction == "right":
            self.__move_left_track(seconds, speed)
        else:
            self.speak("I don't know what direction " + direction + " is. Sorry.")

    # Moves Marvin forward
    def move_forward(self, seconds_to_move=3, speed=5):
        self.__move_right_track(seconds_to_move, speed, False)
        self.__move_left_track(seconds_to_move, speed, False)
        time.sleep(seconds_to_move)

    # Moves Marvin backward
    def move_backward(self, seconds_to_move=3, speed=5):
        speed = speed * (-1)
        self.__move_right_track(seconds_to_move, speed, False)
        self.__move_left_track(seconds_to_move, speed, False)
        time.sleep(seconds_to_move)

    @staticmethod
    def wait(seconds=5):
        time.sleep(seconds)

    # Prints to Marvin's screen
    def print_to_screen(self, statement="Hello everyone!"):
        # sets up the console
        self.__reset_console()
        self.__set_cursor(self._off)
        self.__set_font('Lat15-Terminus24x12')

        # print something to the screen of the device
        print(statement)

        # Sleeps the terminal
        time.sleep(5)

    # Marvin will speak to you
    @staticmethod
    def speak(statement="Hello. I am Marvin. Nice to meet you."):
        ev3.Sound.speak(statement).wait()


# Added a unique class for the Ev3rstorm Mindstorm. Inherits from Robot class
class Optimus(Robot):

    # This just spins the little thing in the arm. Not sure of the purpose of this yet
    _left_arm = "OutA"

    def __init__(self):
        Robot.__init__(self)

    @staticmethod
    def _help():
        method_list = [func for func in dir(Optimus) if callable(getattr(Optimus, func)) and not func.startswith("_")]
        print(method_list)

    def turn(self, direction, degrees=90, seconds=1, speed=6):
        degree_factor = 0.016667
        seconds = degree_factor * degrees * seconds
        Robot._turn(self, direction, speed, seconds)


# Added a unique class for the Gripp3r Mindstorm. Inherits from the Robot Class
class Marvin(Robot):
    # Constants
    _gripper_motor = "outA"

    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        Robot.__init__(self, left_track, right_track)
        self._gripper_motor = gripper_motor

    @staticmethod
    def _help():
        method_list = [func for func in dir(Marvin) if callable(getattr(Marvin, func)) and not func.startswith("_")]
        print(method_list)

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

    def turn(self, direction, degrees=90, seconds=1, speed=6):
        degree_factor = 0.01
        seconds = degree_factor * degrees * seconds
        Robot._turn(self, direction, speed, seconds)

    # TODO - Not yet ready to be implemented.
    @staticmethod
    def _shoot_ball():
        print("Not yet defined!")