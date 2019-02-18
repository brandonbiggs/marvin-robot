######################################################
# Brandon Biggs
# Idaho State University
# This is to get people familiar with Marvin, without the Robot
######################################################
# MarvinJunior Framework

import turtle as t
import time
import pyttsx3
import math

class MarvinJunior:
    height = 0
    width = 0
    turtle = 0
    screen = 0
    marvin_program = ""

    def print_marvin_program(self):
        print(self.marvin_program)

    def __init__(self):
        self.turtle = t.Turtle()
        self.screen = t.Screen()
        self.height = self.screen.window_height()
        self.width = self.screen.window_width()
        self.turtle.shape("turtle")
        self.turtle.shapesize(2, 2)
        self.marvin_program = "#!/usr/bin/env python3 \n" \
                              "##############################\n" \
                              "# Generated Marvin wrapped python file to run robot.\n" \
                              "# Put this file on the robot, make sure this file has proper permissions\n" \
                              "and hit run!\n" \
                              "##############################\n" \
                              "marvin = Marvin()\n"

    def print_screen_size(self):
        print("The current height of the drawable area is " + str(self.height))
        print("The current width of the drawable area is " + str(self.width))

    @staticmethod
    def speak(statement):
        try:
            engine = pyttsx3.init()
            engine.say(statement)
            engine.runAndWait()
        except ImportError:
            print("Failure: pyttsx3 had an issue. May need to install a proper package.")

    # Make sure turtle doesn't go off screen
    # Not yet fully tested. Has some bugs
    def ensure_turtle_boundaries(self, distance, direction_heading):
        half_width = self.width/2
        half_height = self.height/2

        new_x_coord = (math.cos(math.radians(direction_heading))*distance)
        new_y_coord = (math.sin(math.radians(direction_heading))*distance)
        coords = [new_x_coord, new_y_coord]
        print("New coords: (", new_x_coord, ", ", new_y_coord, ")")

        if new_x_coord > half_width:
            # print("X too big")
            coords[0] = half_width - 40

        if new_x_coord < -1*half_width:
            coords[0] = -1*half_width + 40
            # print("X too small")

        if new_y_coord > half_height:
            coords[1] = half_height - 40
            # print("Y too big")

        if new_y_coord < -1*half_height:
            coords[1] = -1 * half_height + 40
            # print("Y too small")
        return coords

    # I didn't want a sleep every single time the turtle tries to move.
    # Besides, I would have thought as a younger kid it would be cool to say "EXECUTE ACTIONS" or something similar
    @staticmethod
    def execute():
        time.sleep(2)

    # Time to move formula may need to be tweaked. I'm not sure how to make turtle move for certain number of seconds
    # Doesn't quite yet work with boundary checking
    def move(self, time_to_move, speed):
        if speed > 10:
            speed = 10
        elif speed <= 0:
            speed = 0
        else:
            speed = math.log(speed) + 1
        self.turtle.speed(speed)
        # print("Turtle position: ", self.turtle.position())

        self.turtle.right(195)
        self.turtle.forward(100)

        turtle_coordinates = self.ensure_turtle_boundaries(time_to_move * 20, self.turtle.heading())
        self.turtle.goto(turtle_coordinates[0], turtle_coordinates[1])
        time.sleep(1)

    # TODO
    def move_left_track(self, time_to_move, speed, sleep=True):
        time = seconds, speed = 1-10

        # movement_time = time_to_move*1000
        # movement_speed = speed*100
        # motor = ev3.Motor(self._left_track)
        # motor.run_timed(time_sp=movement_time, speed_sp=movement_speed)
        # if sleep:
        #     time.sleep(time_to_move)

    def test(self):
        self.turtle.right(90)

        # self.turtle.forward(100)
        time.sleep(5)
        # self.turtle.write("Home = ", False, align="center")
        # self.screen.title("Welcome to the turtle zoo!")
        # time.sleep(5)
        # self.turtle.forward(self.height / 2 - 10)
        # self.turtle.right(90)
        # self.turtle.forward(self.width - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.height - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.width - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.height / 2 - 10)

    def print_to_screen(self, statement):
        self.marvin_program += "marvin.print_to_screen(\"" + statement + "\")\n"
        self.turtle.write(statement, False, align="left")
        time.sleep(3)
