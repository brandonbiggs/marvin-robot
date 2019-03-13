#!/usr/bin/env python3
######################################################
# Brandon Biggs
# This is where the magic happens
######################################################
# Marvin Framework/Wrapper

"""
Function:

Keyword arguments:

"""

import os
import sys
import time
import random

try:
    import ev3dev.ev3 as ev3
except ImportError:
    print("Can't find ev3dev package")


class Robot:
    """
    Base class for controlling Lego Mindstorms. The code is hopefully
            documented well enough to explain what's going on. Otherwise
            visit our website that is meant for using the program.
            https://brandonbiggs.github.io/marvin-robot/
    """

    ###############################################
    # Setup initial settings for robot
    _left_track = "outB"            # Left motor
    _right_track = "outC"           # Right motor
    _DEBUG = False

    ###############################################
    # Prewritten songs
    # Songs are different from tones in their implementation. Songs and tones are
    #       a series of beeps, differing only in their creation format

    # Short Star wars intro
    _short_sw_intro = (
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('G4', 'h'),
        ('D5', 'h'))

    # Long star wars intro
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

    # Keep track of all short and long songs
    _short_songs = [_short_sw_intro, ]
    _long_songs = [_long_sw_intro, ]

    ###############################################
    # Prewritten Tones
    #   Songs and tones are a series of beeps, differing only in their creation format

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

    # Keep track of all short and long tones
    _short_tones = [_long_dv_tone]
    _long_tones = [_long_dv_tone]

    ###############################################
    # Battery Information

    _max_volts = 9.10
    _measured_volts = 0.00
    _min_volts = 5.00

    ###############################################
    # Init

    def __init__(self, left_track="outB", right_track="outC", debug=False):
        """
        Initialization of the robot class

        Keyword arguments:
            left_track -- this is the motor that is connected to the left robot track.
            right_track -- this is the motor that is connected to the right robot track.
                track options are "outA", "outB", "outC", and "outD". Should be visible on the
                mindstorm
            debug -- allows the code to be ran on a computer with output that displays
                what will be ran on the robot when the code is copied to it.
        """
        self._left_track = left_track
        self._right_track = right_track
        self._DEBUG = debug

        # Measure battery information
        if not debug:
            self.__check_battery_level()

    ###############################################
    # Printing functions

    @staticmethod
    def __reset_console():
        """
        Resets the console to the default state
        """
        print('\x1Bc', end="")

    @staticmethod
    def __set_cursor(state):
        """
        Turn the cursor on or off on the screen
        """
        if state:
            print('\x1B[?25h', end='')
        else:
            print('\x1B[?25l', end='')

    @staticmethod
    def __set_font(name='Lat15-Terminus24x12'):
        """
        Sets the console font
            A full list of fonts can be found with `ls /usr/share/consolefonts`

        """
        os.system('setfont ' + name)

    def print_to_screen(self, statement="Hello everyone!"):
        """
        Prints to the Mindstorm console screen

        Keyword arguments:
            statement -- the string that will be printed to the console
        """

        # Ensures statement is string
        statement = str(statement)

        # Prints out the statement
        if self._DEBUG:
            print("DEBUG: This statement will be printed to the screen:", statement)
        else:
            # sets up the console
            self.__reset_console()
            self.__set_cursor(False)
            self.__set_font('Lat15-Terminus24x12')

            # print something to the screen of the device
            print(statement)

            # Sleeps the terminal
            time.sleep(5)

    ###############################################
    # Battery Functions

    def __get_battery_info(self):
        """
        Gets information about the battery from the robot.
        Currently only provides measured volts. Could produce later.
        """
        ps = ev3.PowerSupply()
        self._measured_volts = ps.measured_volts

    def __check_battery_level(self):
        """
        Tells the user if the battery on the robot is getting low
        """
        self.__get_battery_info()
        if self._measured_volts < self._max_volts * 0.6:
            self.speak("Battery getting low.")

    ###############################################
    # Speaker Functions

    def set_speaker_volume(self, volume=80):
        """
        Set volume of robot speaker - Doesn't work for song or tones yet

        Keyword arguments:
            volume -- int between 0 and 100, which the speaker volume will be set to

        """

        # Ensures volume is an int
        if type(volume) is not int:
            volume = 80
            if self._DEBUG:
                print("DEBUG: Volume was not a number.")
                print("DEBUG: EXITING.")
                return None
            else:
                self.print_to_screen("Volume was not a number.")
                return None

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
            time.sleep(3)

    def beep(self, number_of_beeps=1, override=False):
        """
        Produces an audible beep from the robots speakers.

        Keyword arguments:
            number_of_beeps -- number of audible beeps
            override -- Soft cap of 15 beeps unless set to True
        """

        # Ensures that beeps is proper datatype
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
                ev3.Sound.beep().wait()

    def play_random_tone(self, length="long"):
        """
        Plays a random short or long tune. These are a series of beeps
            but different from a song in the way they are created and output

        Keyword arguments:
            length -- play a "short" or "long" random tone
        """

        # Clean up length string just in case
        length = str(length).lower().lstrip().rstrip()

        if self._DEBUG:
            print("DEBUG: length input:", length)

        # Plays a random short tone
        if length == "short":
            random_number = random.randint(0, (len(self._short_tones) - 1))
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
            else:
                self.speak("Sorry, I don't understand the length input of " + length)
            # ev3.Sound.tone(self._short_tones[0])

    def sing_random_song(self, length="short"):
        """
        Plays a random short or long song. These are a series of beeps
            but different from a tone in the way they are created and output

        Keyword arguments:
            length -- play a "short" or "long" random song
        """

        # Normalize length
        length = str(length).lower().rstrip().lstrip()

        if self._DEBUG:
            print("DEBUG: length input was:", length)

        # Play a random short song
        if length == "short":
            random_number = random.randint(0, (len(self._short_songs) - 1))
            if self._DEBUG:
                print("DEBUG: Short song selected.")
            else:
                self.speak("Playing random short song.")
                ev3.Sound.play_song(self._short_songs[random_number]).wait()

        # Play a random long song
        elif length == "long":
            random_number = random.randint(0, (len(self._long_songs) - 1))
            if self._DEBUG:
                print("DEBUG: Long song selected.")
            else:
                self.speak("Playing random long song.")
                ev3.Sound.play_song(self._long_songs[random_number]).wait()

        # Play the first short song if the parameter is wrong
        else:
            if self._DEBUG:
                print("DEBUG: Invalid length.")
                print("DEBUG: Playing first short song.")
            else:
                self.speak("I don't understand the length requested. Playing random short song.")
                ev3.Sound.play_song(self._short_songs[0]).wait()

    def speak(self, statement="Hello. I am Marvin. Nice to meet you."):
        """
        Outputs the statement through the mindstorm speaker

        Keyword arguments:
            statement -- whatever is passed here will be spoken through the speaker
        """

        # Ensure that statement is a string
        statement = str(statement)

        # Output statement
        if self._DEBUG:
            print("DEBUG: Statement that will be spoken is:", statement)
        else:
            ev3.Sound.speak(statement).wait()

    # TODO - Write function for people to write their own songs
    # def write_song():

    # TODO - Write function for people to write their own tones
    # def write_tone():

    ###############################################
    # Movement Functions

    @staticmethod
    def __get_tachos_from_speed(speed, surface_factor=0):
        """
        Get a number of tacho units per rotation.
        Tacho units are a way of measuring motor movement.

        Different speeds take different tacho units to turn the track one full rotation
        because of spin up and down times.

        Keyword arguments:
            speed -- speed that tacho motor will run at
            surface_factor -- designed to increase or decrease the amount of tacho units
                it takes to turn one full rotation. Small +/- number to get the robot closer to
                one full rotation
                I tested this on a mostly hard surface, but carpet may change things.
        """
        tacho_counts = 0 + surface_factor
        if speed == 1:
            tacho_counts = 1070 + surface_factor
        if speed == 2:
            tacho_counts = 1050 + surface_factor
        if speed == 3:
            tacho_counts = 1030 + surface_factor
        if speed == 4:
            tacho_counts = 985 + surface_factor
        if speed == 5:
            tacho_counts = 930 + surface_factor
        if speed == 6:
            tacho_counts = 885 + surface_factor
        if speed == 7:
            tacho_counts = 840 + surface_factor
        if speed == 8:
            tacho_counts = 820 + surface_factor
        if speed == 9:
            tacho_counts = 805 + surface_factor
        if speed == 10:
            tacho_counts = 800 + surface_factor
        return tacho_counts

    def __move_left_track(self, distance, speed, sleep=True):
        """
        Moves the left track of the robot based on the motor it's hooked to. The motor that
        controls the left and right tracks were established on init

        Keyword arguments:
            distance -- count of tacho units that the motor will be moved
            speed -- speed that tacho motor will run at
            sleep -- True makes the program wait until the motor is finished. Otherwise, proceed.
                This is important for turning vs moving forward. If moving forward, both motors
                can't be set to sleep or it will just turn instead of move forward
        """
        self.__move_track(distance, speed, self._left_track, sleep)

    def __move_right_track(self, distance, speed, sleep=True):
        """
        Moves the right track of the robot based on the motor it's hooked to. The motor that
        controls the left and right tracks were established on init

        Keyword arguments:
            distance -- count of tacho units that the motor will be moved
            speed -- speed that tacho motor will run at
            sleep -- True makes the program wait until the motor is finished. Otherwise, proceed.
                This is important for turning vs moving forward. If moving forward, both motors
                can't be set to sleep or it will just turn instead of move forward
        """
        self.__move_track(distance, speed, self._right_track, sleep)

    def __move_track(self, distance, speed, track, sleep=True):
        """
        Moves the specified track of the robot based on the motor it's hooked to. The motor that
        controls the left and right tracks were established on init

        Keyword arguments:
            distance -- count of tacho units that the motor will be moved
            speed -- speed that tacho motor will run at
            track -- left or right motor
            sleep -- True makes the program wait until the motor is finished. Otherwise, proceed.
                This is important for turning vs moving forward. If moving forward, both motors
                can't be set to sleep or it will just turn instead of move forward
        """
        if self._DEBUG:
            print("DEBUG: Distance -", distance, "speed:", speed, "track:", track)
            return None

        # Execute EV3 action
        motor = ev3.Motor(track)
        motor.reset()
        motor.run_to_abs_pos(position_sp=distance, speed_sp=speed)

        if sleep:
            # Waits until the motor is finished running
            while motor.is_running:
                time.sleep(1)

    def turn(self, direction, speed=3, degrees=90, surface_factor=0):
        """
        Turns the robot using just one track, specified with "direction".

        Keyword arguments:
            direction -- "left" or "right" direction in which robot will turn
            speed -- 1 to 10, speed in which robot will do the turning
            degrees -- number of degrees robot will turn
            surface_factor -- This is where things get tricky. This is a small +/- int
                that will help ensure that the robot is making a full rotation
                on the surface that it is on. If it appears that the robot isn't
                making a full rotation, add a small positive number here, ex. 10
                and then test again. If it's moving further than a rotation, add
                a small negative number here, ex. -10. When testing the robot,
                I tried using a surface where the robot wouldn't get slowed down
                like it would on carpet, but it's not perfect. This set to zero
                should be pretty good.
        """
        # tacho count/turn_degrees = number of tachos to turn one degree
        default_turn_degrees = 110

        # Normalize direction
        direction = str(direction).lower().lstrip().rstrip()

        # Ensure that speed is a bounded int
        if type(speed) is not int:
            if self._DEBUG:
                print("DEBUG: Unknown speed")
            return None
        if speed > 10:
            if self._DEBUG:
                print("DEBUG: Speed too high. Setting speed to 10.")
            speed = 10
        if speed < 0:
            if self._DEBUG:
                print("DEBUG: Speed to low. Setting speed to 1.")
            speed = 1
            # movement_time = time_to_move * 1000

        tacho_count = self.__get_tachos_from_speed(speed, surface_factor)

        if self._DEBUG:
            print("DEBUG: speed:", speed, "tacho count:", tacho_count, "degrees: ", degrees, "default turn degrees:",
                  default_turn_degrees)

        # Moves the robot motor x tacho units
        movement_tachos = tacho_count / default_turn_degrees * degrees

        # Multiply speed by 100 as the ev3 motor interprets the speed in increments of 100's
        movement_speed = speed * 100

        if self._DEBUG:
            if direction == "left" or direction == "right":
                print("DEBUG: Robot will turn", direction, "at speed", speed)
                self.__move_right_track(movement_tachos, movement_speed)
                self
            else:
                print("DEBUG: Unknown direction", direction)
            return None

        # To turn left, you have to move the right track forward
        if direction == "left":
            self.__move_right_track(movement_tachos, movement_speed)

        # To turn right, you have to move the left track forward
        elif direction == "right":
            self.__move_left_track(movement_tachos, movement_speed)

        # if direction isn't left or right
        else:
            self.speak("I don't know what direction " + direction + " is. Sorry.")

    def move_forward(self, distance_in_feet=1.0, speed=3, override=False, surface_factor=0):
        """
        TODO - Run final test
        Move the robot forward based on distance in feet

        Keyword arguments:
            distance_in_feet -- feet that robot will travel with soft cap of 15ft
            speed -- speed in which robot will travel 1 to 10
            override -- remove the soft cap from distance_in_feet
            surface_factor -- This is where things get tricky. This is a small +/- int
                that will help ensure that the robot is making a full rotation
                on the surface that it is on. If it appears that the robot isn't
                making a full rotation, add a small positive number here, ex. 10
                and then test again. If it's moving further than a rotation, add
                a small negative number here, ex. -10. When testing the robot,
                I tried using a surface where the robot wouldn't get slowed down
                like it would on carpet, but it's not perfect. This set to zero
                should be pretty good.
        """

        # Ensure that speed is a bounded int
        if type(speed) is not int:
            speed = 3
            if self._DEBUG:
                print("DEBUG: Unknown speed")
        if speed > 10:
            if self._DEBUG:
                print("DEBUG: Speed too high. Setting speed to 10.")
            speed = 10
        if speed < 0:
            if self._DEBUG:
                print("DEBUG: Speed too low. Setting speed to 1.")
            speed = 1

        # Ensure distance is bounded and type checked
        if type(distance_in_feet) is int:
            distance_in_feet = float(distance_in_feet)
        if type(distance_in_feet) is not float:
            if self._DEBUG:
                print("DEBUG: Unknown feet distance")
            return None
        if distance_in_feet > 15.0:
            if self._DEBUG:
                print("DEBUG: distance > 15. Setting distance = 15, unless override = true.")
            if not override:
                distance_in_feet = 15.0
        if distance_in_feet < 0.0:
            if self._DEBUG:
                print("DEBUG: distance too low. Setting distance to 1 foot.")
            distance_in_feet = 1.0

        # Calculates how many tacho units is one rotation
        tacho_count = self.__get_tachos_from_speed(speed, surface_factor)

        if self._DEBUG:
            print("DEBUG: Moving forward!")
            print("DEBUG: speed:", speed, "tacho count:", tacho_count)
            return None

        # Moves the robot motor x tacho units * number of feet
        movement_tachos = tacho_count * distance_in_feet
        # Multiply speed by 100 as the ev3 motor interprets the speed in increments of 100's
        movement_speed = speed * 100

        # Move both tracks and don't sleep the first one
        self.__move_left_track(movement_tachos, movement_speed, sleep=False)
        self.__move_right_track(movement_tachos, movement_speed)

    def move_backward(self, distance_in_feet=1.0, speed=3, override=False, surface_factor=0):
        """
        TODO - Run final tests

        Move the robot backward based on distance in feet

        Keyword arguments:
            distance_in_feet -- feet that robot will travel with soft cap of 15ft
            speed -- speed in which robot will travel 1 to 10
            override -- remove the soft cap from distance_in_feet
            surface_factor -- This is where things get tricky. This is a small +/- int
                that will help ensure that the robot is making a full rotation
                on the surface that it is on. If it appears that the robot isn't
                making a full rotation, add a small positive number here, ex. 10
                and then test again. If it's moving further than a rotation, add
                a small negative number here, ex. -10. When testing the robot,
                I tried using a surface where the robot wouldn't get slowed down
                like it would on carpet, but it's not perfect. This set to zero
                should be pretty good.
        """

        # Ensure that speed is a bounded int
        if type(speed) is not int:
            if self._DEBUG:
                print("DEBUG: Unknown speed")
            return None
        if speed > 10:
            if self._DEBUG:
                print("DEBUG: Speed too high. Setting speed to 10.")
            speed = 10
        if speed < 0:
            if self._DEBUG:
                print("DEBUG: Speed too low. Setting speed to 1.")
            speed = 1

        # Ensure distance is bounded and type checked
        if type(distance_in_feet) is int:
            distance_in_feet = float(distance_in_feet)
        if type(distance_in_feet) is not float:
            if self._DEBUG:
                print("DEBUG: Unknown feet distance")
            return None
        if distance_in_feet > 15.0:
            if self._DEBUG:
                print("DEBUG: distance > 15. Setting distance = 15, unless override = true.")
            if not override:
                distance_in_feet = 15.0
        if distance_in_feet < 0.0:
            if self._DEBUG:
                print("DEBUG: distance too low. Setting distance to 1 foot.")
            distance_in_feet = 1.0

        # Calculates how many tacho units is one rotation
        tacho_count = self.__get_tachos_from_speed(speed, surface_factor)

        if self._DEBUG:
            print("DEBUG: Moving forward!")
            print("DEBUG: speed:", speed, "tacho count:", tacho_count)
            return None

        # Moves the robot motor x tacho units * num feet * -1 to move it in reverse
        movement_tachos = tacho_count * distance_in_feet * -1
        # Multiply speed by 100 as the ev3 motor interprets the speed in increments of 100's
        movement_speed = speed * 100

        # Move both tracks and don't sleep the first one
        self.__move_left_track(movement_tachos, movement_speed, sleep=False)
        self.__move_right_track(movement_tachos, movement_speed)

    ###############################################
    # Button Functions

    def set_button_colors(self, color="green", button="left", brightness=100):
        """
        Sets LEDs of robot's left or right buttons to specified colors

        Keyword arguments:
            color -- 6 Different colors can be used. Options are:
                BLACK, RED, GREEN, AMBER, ORANGE, YELLOW
            button -- 2 Different buttons, 'LEFT' or 'RIGHT'
            brightness -- integer, 0 to 100 for brightness, 0 - none, 100 - max
        """

        # Cleaning up color string and button string
        color = str(color).lower().lstrip().rstrip()
        button = str(button).lower().lstrip().rstrip()

        # Setting color and button arrays
        colors = ["black", "red", "green", "amber", "orange", "yellow"]
        buttons = ["right", "left"]

        # Print color and button
        if self._DEBUG:
            print("DEBUG: color: ", color)
            print("DEBUG: button: ", button)

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

        # Ensures brightness is valid - set to max if invalid
        if type(brightness) is not int:
            brightness = 100
            if self._DEBUG:
                print("DEBUG: Brightness was not an int. Setting brightness to 100.")
            else:
                self.print_to_screen("brightness set to 100.")

        # Checks limits on brightness
        if brightness < 0:
            brightness = 0
        if brightness > 100:
            brightness = 100

        # Set colors of buttons
        if self._DEBUG:
            print("DEBUG:", button, "button set to", color, "color with", brightness, " brightness.")
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

    ###############################################
    # Auxiliary Functions

    def wait(self, seconds=5):
        """
        Pauses actions of the robot for given time in seconds

        Keyword arguments:
            seconds -- number of seconds that the robot will pause, up to 30 seconds
        """

        # Ensures that seconds is an int
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

        # Wait
        if self._DEBUG:
            print("DEBUG: wait time set to:", seconds, "seconds.")
        else:
            time.sleep(seconds)

    ###############################################
    # Demo Functions

    def demo_racecar(self):
        """
        Turn the robot into a mini racecar
        """
        if self._DEBUG:
            print("DEBUG: being a racecar!")
        else:
            self.speak("Starting my engines!")
            self.demo_play_sound("car")
            self.move_forward(distance_in_feet=.1, speed=10)
            self.speak("VROOM VROOM")
            self.move_backward(distance_in_feet=.1, speed=10)

    def demo_dance(self):
        """
        Tries to dance
        """
        if self._DEBUG:
            print("DEBUG: doing robot dance")
        else:
            self.speak("Lets dance!")
            self.turn("right", speed=10, degrees=15)
            self.move_forward(distance_in_feet=.1, speed=10)
            self.move_backward(distance_in_feet=.1, speed=10)
            self.move_forward(distance_in_feet=.1, speed=10)
            self.move_backward(distance_in_feet=.1, speed=10)
            self.turn("left", speed=10, degrees=720)
            self.speak("Woohoo! That was a fun dance.")

    def demo_babyshark(self):
        """
        Plays a few lines of baby shark
        """
        song = "Baby shark, doo doo doo doo" + \
            "Mommy shark, doo doo doo doo" + \
            "Daddy shark, doo doo doo doo"
        if self._DEBUG:
            print("DEBUG: playing babyshark.")
        else:
            self.speak(song)

    def demo_play_sound(self, name="car"):
        """
        Plays a demo sound

        Keyword arguments:
            name -- this is the nickname for the name of the file you want to play
                "car" -- plays wav of a car starting
                "sneeze" -- plays wav of a man sneezing
        """
        if name == "car":
            wav_file = "car.wav"
        elif name == "sneeze":
            wav_file = "sneeze.man.wav"
        else: wav_file = "car.wav"

        if self._DEBUG:
            print("DEBUG: playing wav file:", wav_file)
        else:
            ev3.Sound.play("/home/robot/marvin-wrapper/modules/sounds/" + wav_file).wait()


class Everstorm(Robot):
    """
    Added a unique class for the Ev3rstorm Mindstorm. Inherits from Robot class
    """
    _DEBUG = False

    # This just spins the little thing in the arm. Not sure of the purpose of this yet
    _left_arm = "OutA"

    def __init__(self, debug=False):
        """
        Added a unique class for the Gripp3r Mindstorm. Inherits from the Robot Class
        """
        Robot.__init__(self)
        self._DEBUG = debug

    @staticmethod
    def _help():
        """
        Supposed to list all of the possible functions.
        Not sure if it's helpful or not yet
        """
        method_list = [func for func in dir(Everstorm) if
                       callable(getattr(Everstorm, func)) and not func.startswith("_")]
        print(method_list)


class Gripper(Robot):
    """
    Added a unique class for the Gripp3r Mindstorm. Inherits from the Robot Class
    """
    _DEBUG = False
    # Constants
    _gripper_motor = "outA"

    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC", debug=False):
        """
        Sets the proper class variables for the gripper
        """
        Robot.__init__(self, left_track, right_track)
        self._gripper_motor = gripper_motor
        self._DEBUG = debug

    @staticmethod
    def _help():
        """
        Supposed to list all of the possible functions.
        Not sure if it's helpful or not yet
        """
        method_list = [func for func in dir(Gripper) if callable(getattr(Gripper, func)) and not func.startswith("_")]
        print(method_list)

    def open_hands(self):
        """
        opens the gripper claws of the gripp3r mindstorm
        TODO - Setup error checking
        """

        time_to_run = 3000
        speed = -800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run / 1000 + 1)

    def close_hands(self):
        """
        closes the gripper claws of the gripp3r mindstorm
        TODO - Setup error checking
        """
        time_to_run = 3000
        speed = 800
        motor = ev3.MediumMotor(self._gripper_motor)
        motor.run_timed(time_sp=time_to_run, speed_sp=speed)
        time.sleep(time_to_run / 1000 + 1)


class Marvin(Gripper):
    """
    Class for Gripper just in case someone still wants to call it Marvin
    """
    def __init__(self, gripper_motor="outA", left_track="outB", right_track="outC"):
        Gripper.__init__(self, gripper_motor=gripper_motor, left_track=left_track, right_track=right_track)


class Optimus(Everstorm):
    """
    Class for Everstorm just in case someone still wants to call it Optimus
    TODO - Test
    """
    def __init__(self):
        Everstorm.__init__(self)
