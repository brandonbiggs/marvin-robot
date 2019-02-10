# marvin-robot
This is an incredibly simplified wrapper for the Lego Mindstorm ev3dev project. The purpose of this wrapper is to help beginning programmers understand syntax of programming while also applying it to something physical that they can play with using the Mindstorm robots.

# TODO - 
## Setup
1. Build your mindstorm Robot - https://www.lego.com/en-us/mindstorms/build-a-robot
2. Flash the ev3dev image to an SD card - https://www.ev3dev.org/
3. Ensure that the ev3dev image loads on the mindstorm robot
4. ...

# Examples:
The following 4 lines will move the mindstorm robot forward, have it say 
"Hello world" and then move back to it's original starting point. 
The purpose here is to demonstrate what programming can do, while doing so 
in as simple lines as possible. 

marvin = Marvin()

marvin.moveForward(7, 7)

marvin.speak("Hello world!")

marvin.moveBackward(7,7)
