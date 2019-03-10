#!/usr/bin/env python3
######################################################
# Brandon Biggs
# This is where the magic happens
######################################################
# Marvin Framework/Wrapper

import os
import sys
import time
import random

try:
    import ev3dev.ev3 as ev3
except ImportError:
    print("Can't find ev3dev package")


# Base class for controlling the Mindstorms
class Robot:
    ###############################################
    # Setup initial settings for robot
    _left_track = "outB"            # Left motor
    _right_track = "outC"           # Right motor
    _cursor_on = True               # Cursor static setting
    _cursor_off = False             # Cursor static setting
    _DEBUG = False

    ###############################################
    # Prewritten songs
    # Songs are different from tones in their implementation. Songs are
    #       a series of beeps in different tones while tones are something else

    # Short Star wars into
    _short_sw_intro = (
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('G4', 'h'),
        ('D5', 'h'))

    _long_sw_intro = (
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('G4', 'h'),
        ('D5', 'h'),
        ('C5', 'e3'),
        ('B4', 'e3'),
        ('A4', 'e3'),
        ('G5', 'h'),
        ('D5', 'q'),
        ('C5', 'e3'),
        ('B4', 'e3'),
        ('A4', 'e3'),
        ('G5', 'h'),
        ('D5', 'q'),
        ('C5', 'e3'),
        ('B4', 'e3'),
        ('C5', 'e3'),
        ('A4', 'h.'),)

    _short_songs = [_short_sw_intro, ]
    _long_songs = [_long_sw_intro, ]

    ###############################################
    # Prewritten Tones

    # Darth Vader Tone
    _long_dv_tone = [
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
    ]

    _short_tones = [_long_dv_tone]
    _long_tones = [_long_dv_tone]

    ###############################################
    # Functions

    # Init
    def __init__(self, left_track="outB", right_track="outC", debug=False):
        self._left_track = left_track
        self._right_track = right_track
        self._DEBUG = debug

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

    # TODO - Test on robot
    # Produces a beep
    def beep(self, number_of_beeps=1, override=False):
        # Ensures that beeps is an int
        if type(number_of_beeps) is not int:
            if self._DEBUG:
                print("DEBUG: incorrect datatype for number of beeps.")
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Unknown beep count")
                print("DEBUG: EXITING.")
                return None

        # If seconds is int, check bounds
        if number_of_beeps < 0:
            if self._DEBUG:
                print("DEBUG: Number of beeps was negative. Setting to 1.")
            number_of_beeps = 1
        if number_of_beeps > 15 and not override:
            if self._DEBUG:
                print("DEBUG: Number of beeps was larger than 15. Setting to 15.")
            number_of_beeps = 15
        if override:
            if self._DEBUG:
                print("DEBUG: Number of beeps was larger than 15 and override was set to true. Prepare for many beeps.")

        # Make Mindstorm beep
        if self._DEBUG:
            print("DEBUG: Number of beeps:", number_of_beeps)
        else:
            for _ in range(number_of_beeps):
                ev3.Sound.beep()

    # TODO - Test with Robot
    # Plays a random short or long Tone
    def play_random_tone(self, length="long"):
        # Clean up length stream just in case
        length = str(length).lower().lstrip().rstrip()
        if self._DEBUG:
            print("DEBUG: length input:", length)

        # Plays a random short tone
        if length == "short":
            random_number = random.randint(0, (len(self._short_tones) - 1))
            # print("random number: ", random_number)
            if self._DEBUG:
                print("DEBUG: Random short tone selected.")
                print("DEBUG: No short tone yet!")
            else:
                # ev3.Sound.tone(self._short_tone[random_number]).wait()
                self.speak("Sorry, there are no short tones yet.")

        # Play a random long tone
        elif length == "long":
            random_number = random.randint(0, (len(self._long_tones) - 1))
            if self._DEBUG:
                print("DEBUG: Random long tone selected.")
            else:
                ev3.Sound.tone(self._long_tones[random_number]).wait()

        # Incorrect input
        else:
            if self._DEBUG:
                print("DEBUG: Invalid input.")
                print("DEBUG: Playing first short tone.")
            # else:
            # ev3.Sound.tone(self._short_tones[0])

    # TODO - Test on robot
    # Prints to the Mindstorm screen
    def print_to_screen(self, statement="Hello everyone!"):
        # Ensures statement is string
        statement = str(statement)

        # Prints out the statement
        if self._DEBUG:
            print("DEBUG: This statement will be printed to the screen:", statement)
        else:
            # sets up the console
            self.__reset_console()
            self.__set_cursor(self._cursor_off)
            self.__set_font('Lat15-Terminus24x12')

            # print something to the screen of the device
            print(statement)

            # Sleeps the terminal
            time.sleep(5)

    # TODO - Test on robot
    # Sets colors of robots buttons
    def set_button_colors(self, color="green", button="left", brightness=100):
        # All possible Color Objects
        # BLACK = ( 0, 0, )
        # RED = ( 1, 0, )
        # GREEN = ( 0, 1, )
        # AMBER = ( 1, 1, )
        # ORANGE = ( 1, 0.5, )
        # YELLOW = ( 0.1, 1, )

        # All possible Buttons Objects
        # LEFT = (red_left, green_left,)
        # RIGHT = (red_right, green_right,)

        # Cleaning up color string and button string
        color = str(color).lower().lstrip().rstrip()
        button = str(button).lower().lstrip().rstrip()

        # Print color and button
        if self._DEBUG:
            print("DEBUG: color: ", color)
            print("DEBUG: button: ", button)

        # Setting color and button arrays
        colors = ["black", "red", "green", "amber", "orange", "yellow"]
        buttons = ["right", "left"]

        # Ensures button is valid - exit if not
        if button not in buttons:
            if self._DEBUG:
                print("DEBUG: Unknown button:", button)
                print("DEBUG: Please use 'left' or 'right'.")
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Unknown button:" + str(button))
                print("DEBUG: EXITING.")
                return None

        # Ensures color is valid - exit if not
        if color not in colors:
            if self._DEBUG:
                print("DEBUG: Unknown color. Please use one of the following: ", colors)
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Unknown button: " + str(color))
                print("DEBUG: EXITING.")
                return None

        # Ensures brightness is valid - don't exit as invalid brightness can be fixed easily
        if type(brightness) is not int:
            brightness = 100
            if self._DEBUG:
                print("DEBUG: Brightness was not an int. Setting brightness to 100.")
            else:
                self.print_to_screen("Unknown brightness " + str(brightness) + " setting brightness to 100.")
        # Checks limits on brightness
        if brightness < 0:
            brightness = 0
        if brightness > 100:
            brightness = 100

        # Set colors of buttons
        if self._DEBUG:
            print("DEBUG: Setting ", button, " button to ", color, " color with ", brightness, " brightness.")
        else:
            # Set defaults just in case something goes wrong below
            ev3_color = ev3.Leds.RED
            ev3_button = ev3.Leds.RIGHT
            # Sets buttons to proper objects
            if button == "left":
                ev3_button = ev3.Leds.LEFT
            if button == "right":
                ev3_button = ev3.Leds.RIGHT
            # Sets colors to proper objects
            if color == "black":
                ev3_color = ev3.Leds.BLACK
            if color == "red":
                ev3_color = ev3.Leds.RED
            if color == "green":
                ev3_color = ev3.Leds.GREEN
            if color == "amber":
                ev3_color = ev3.Leds.AMBER
            if color == "orange":
                ev3_color = ev3.Leds.ORANGE
            if color == "yellow":
                ev3_color = ev3.Leds.YELLOW
            # Finally set colors
            ev3.Leds.set_color(ev3_button, ev3_color, brightness)

    # TODO - Test on robot
    # Set volume of robot speaker
    def set_volume(self, volume=80):
        # Ensures volume is an int
        if type(volume) is not int:
            volume = 80
            if self._DEBUG:
                print("DEBUG: Volume was not a number.")
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Volume was not a number.")

        # Makes Sure volume is within bounds
        if volume < 0:
            if self._DEBUG:
                print("DEBUG: Volume was less than 0. Setting to 0")
            volume = 0
        if volume > 100:
            if self._DEBUG:
                print("DEBUG: Volume was greater than 100. Setting to 100.")
            volume = 100

        # Sets volume for speaker
        if self._DEBUG:
            print("DEBUG: Set volume to: ", volume)
        else:
            ev3.Sound.set_volume(volume)

    # TODO - Test with Robot
    # Plays a random short or long song
    def sing_random_song(self, length="short"):
        length = str(length)
        length = length.lower().rstrip().lstrip()
        if self._DEBUG:
            print("DEBUG: length input was:", length)
        # Play a random short song
        if length == "short":
            random_number = random.randint(0, (len(self._short_songs) - 1))
            # print("random number: ", random_number)
            if self._DEBUG:
                print("DEBUG: Short song selected.")
            else:
                ev3.Sound.play_song(self._short_songs[random_number])
        # Play a random long song
        elif length == "long":
            random_number = random.randint(0, (len(self._long_songs) - 1))
            if self._DEBUG:
                print("DEBUG: Long song selected.")
            else:
                ev3.Sound.play_song(self._long_songs[random_number])
        # Play the first short song if the parameter is wrong
        else:
            if self._DEBUG:
                print("DEBUG: Invalid length.")
                print("DEBUG: Playing first short song.")
            else:
                ev3.Sound.play_song(self._short_songs[0])

    # TODO - Test on robot
    # Outputs the statement through the mindstorm speaker
    def speak(self, statement="Hello. I am Marvin. Nice to meet you."):
        # Ensure that statement is a string
        statement = str(statement)

        # Output statement
        if self._DEBUG:
            print("DEBUG: Statement that will be spoken is:", statement)
        else:
            ev3.Sound.speak(statement).wait()

    # TODO - Test on robot
    # Set wait time
    def wait(self, seconds=5):
        # Ensures that seconds is int
        if type(seconds) is not int:
            if self._DEBUG:
                print("DEBUG: incorrect datatype for seconds.")
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Unknown wait time.")
                print("DEBUG: EXITING.")
                return None
        # If seconds is int, check bounds
        if seconds < 0:
            seconds = 0
        if seconds > 30:
            seconds = 30

        # Wait time
        if self._DEBUG:
            print("DEBUG: wait time set to:", seconds, "seconds.")
        else:
            time.sleep(seconds)

    ###############################################
    # UNTESTED FUNCTIONS

    # Moves the left track
    def __move_left_track(self, time_to_move, speed, sleep=True):
        self.__move_track(time_to_move, speed, self._left_track, sleep)

    # Moves the right Track
    def __move_right_track(self, time_to_move, speed, sleep=True):
        self.__move_track(time_to_move, speed, self._right_track, sleep)

    @staticmethod
    def __move_track(time_to_move, speed, track, sleep=True):
        movement_time = time_to_move * 1000
        movement_speed = speed * 100
        motor = ev3.Motor(track)
        motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        if sleep:
            time.sleep(time_to_move)

    # TODO - Fix turning
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

    # TODO - Change to move based on rotation instead of time
    # Moves Marvin forward
    def move_forward(self, seconds_to_move=3, speed=5):
        if self._DEBUG:
            print("DEBUG: TODO move_forward ")
        else:
            self.__move_right_track(seconds_to_move, speed, False)
            self.__move_left_track(seconds_to_move, speed, False)
            time.sleep(seconds_to_move)

    # TODO - Change to move based on rotation instead of time
    # Moves Marvin backward
    def move_backward(self, seconds_to_move=3, speed=5):
        speed = speed * (-1)
        self.__move_right_track(seconds_to_move, speed, False)
        self.__move_left_track(seconds_to_move, speed, False)
        time.sleep(seconds_to_move)

    # TODO - Write function for people to write their own songs
    # def write_song():

    # TODO - Write function for people to write their own tones
    # def write_tone():


# Added a unique class for the Ev3rstorm Mindstorm. Inherits from Robot class
class Everstorm(Robot):
    # This just spins the little thing in the arm. Not sure of the purpose of this yet
    _left_arm = "OutA"

    def __init__(self):
        Robot.__init__(self)

    @staticmethod
    def _help():
        method_list = [func for func in dir(Everstorm) if
                       callable(getattr(Everstorm, func)) and not func.startswith("_")]
        print(method_list)

    def turn(self, direction, degrees=90, seconds=1, speed=6):
        degree_factor = 0.016667
        seconds = degree_factor * degrees * seconds
        Robot._turn(self, direction, speed, seconds)


# Added a unique class for the Gripp3r Mindstorm. Inherits from the Robot Class
class Gripper(Robot):
    # Constants
    _gripper_motor = "outA"

    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        Robot.__init__(self, left_track, right_track)
        self._gripper_motor = gripper_motor

    @staticmethod
    def _help():
        method_list = [func for func in dir(Gripper) if callable(getattr(Gripper, func)) and not func.startswith("_")]
        print(method_list)

    # Opens Grippers
    def open_hands(self):
        time_to_run = 3000
        speed = -800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run / 1000 + 1)

    # Closes Grippers
    def close_hands(self):
        time_to_run = 3000
        speed = 800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run / 1000 + 1)

    def turn(self, direction, degrees=90, seconds=1, speed=6):
        degree_factor = 0.01
        seconds = degree_factor * degrees * seconds
        Robot._turn(self, direction, speed, seconds)


# Class for Gripper just in case someone still wants to call it Marvin
# TODO - Test
class Marvin(Gripper):
    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        Gripper.__init__(self, left_track, right_track)


# Class for Everstorm just in case someone still wants to call it Optimus
# TODO - Test
class Optimus(Everstorm):
    def __init__(self):
        Everstorm.__init__(self)
