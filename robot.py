#!/usr/bin/env python3
######################################################
# Brandon Biggs
# Create Marvin and have Marvin do fun things!
######################################################

from modules.robot import Marvin

marvin = Marvin()

marvin.print_to_screen("Print to screen!")

marvin.speak("Hello. I am Marvin. Nice to meet you!")

marvin.close_hands()

marvin.open_hands()

marvin.move_forward()

marvin.move_backward()
