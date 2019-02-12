#!/usr/bin/env python3
######################################################
# Brandon Biggs
# Create Marvin and have Marvin do fun things!
######################################################

from modules.marvin import Marvin
# from modules.marvin_junior import MarvinJunior

marvin = Marvin()

marvin.print_to_screen("Print to screen!")

marvin.speak("Hello. I am Marvin. Nice to meet you!")

marvin.close_hands()

marvin.open_hands()

marvin.move_forward(7, 7)

marvin.move_backward(7,7)