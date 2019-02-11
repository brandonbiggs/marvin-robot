#!/usr/bin/env python3
######################################################
# Brandon Biggs
# This is where the magic happens
######################################################
# Marvin Framework

import os
import sys
import time
import ev3dev.ev3 as ev3

class Marvin:
    # Constants
    _on = True
    _off = False
    _gripper_motor = "outA"
    _left_track = "outB"
    _right_track = "outC"

    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        self._gripper_motor = gripper_motor
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
        ev3.Sound.speak(statement)
        time.sleep(5)
    
    # TODO - This isn't appropriately named as it does more than just opens
    @staticmethod
    def open_hands():
        time_to_run = 2000
        speed = 500
        motor = ev3.MediumMotor('outA')
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run/1000)

    # TODO - This isn't appropriately named as it does more than just closes
    @staticmethod
    def close_hands():
        timeToRun = 2000
        speed = -500
        motor = ev3.MediumMotor('outA')
        motor.run_timed(time_sp=timeToRun, speed_sp=speed)
        time.sleep(timeToRun/1000)

    # TODO - Figure out a better way of implementing this
    @staticmethod
    def move_hands(time_to_move, speed, direction):
        # Examples:
        #   moveHands(2, 5, "forward")
        # time_sp - 
        # speed_sp - Sets the speed in tacho counts/second. Negative means run in reverse
        time_to_move = time_to_move*1000
        movement_direction = 1
        if direction == "reverse":
            movement_direction = -1
        speed = speed*movement_direction*100
        
        motor = ev3.MediumMotor('outA')
        motor.run_timed(time_sp=time_to_move, speed_sp=speed)

    # Moves the left track
    def move_left_track(self, time_to_move, speed, sleep=True):
        # time = seconds, speed = 1-10
        movement_time = time_to_move*1000
        movement_speed = speed*100
        motor = ev3.Motor(self._left_track)
        motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        if sleep:
            time.sleep(time_to_move)
    
    # Moves the right Track
    def move_right_track(self, time_to_move, speed, sleep=True):
        movement_time = time_to_move*1000
        movement_speed = speed*100
        motor = ev3.Motor(self._right_track)
        motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        if sleep:
            time.sleep(time_to_move)

    # Moves Marvin forward
    def move_forward(self, time_to_move, speed):
        self.move_right_track(time_to_move, speed, False)
        self.move_left_track(time_to_move, speed, False)
        time.sleep(time_to_move)

    # Moves Marvin backward
    def move_backward(self, time_to_move, speed):
        speed = speed * (-1)
        self.move_right_track(time_to_move, speed, False)
        self.move_left_track(time_to_move, speed, False)
        time.sleep(time_to_move)

    # TODO
    def turn(self, degrees, direction):
        print("Not yet defined!")

    # TODO
    def shoot_ball(self):
        print("Not yet defined!")