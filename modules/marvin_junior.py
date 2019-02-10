######################################################
# Brandon Biggs
# Idaho State University
# This is to get people familiar with Marvin, without the Robot
######################################################
# MarvinJunior Framework

import turtle as t
import time

class MarvinJunior:
    height = 0
    width = 0
    turtle = 0
    screen = 0
    marvinProgram = ""

    def printMarvinProgram(self):
        print(self.marvinProgram)

    def __init__(self):
        self.turtle = t.Turtle()
        self.screen = t.Screen()
        self.height = self.screen.window_height()
        self.width = self.screen.window_width()
        self.marvinProgram = "#!/usr/bin/env python3 \n" \
                             "##############################\n" \
                             "# Generated Marvin wrapped python file to run robot.\n" \
                             "# Put this file on the robot, make sure this file has proper permissions\n" \
                             "and hit run!\n" \
                             "##############################\n" \
                             "marvin = Marvin()\n"

    def printScreenSize(self):
        print("The current height of the drawable area is " + str(self.height))
        print("The current width of the drawable area is " + str(self.width))

    def test(self):
        self.turtle.write("Home = ", False, align="center")
        self.screen.title("Welcome to the turtle zoo!")
        time.sleep(5)
        # self.turtle.forward(self.width / 2 - 10)
        # self.turtle.right(90)
        # self.turtle.forward(self.height / 2 - 10)
        # self.turtle.right(90)
        # self.turtle.forward(self.width - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.height - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.width - 20)
        # self.turtle.right(90)
        # self.turtle.forward(self.height / 2 - 10)

    def move(self):
        print("Not yet defined!")

    def printToScreen(self, statement):
        self.marvinProgram += "marvin.printToScreen(\"" + statement + "\")\n"
        self.turtle.write(statement, False, align="left")
        time.sleep(3)