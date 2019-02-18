# Marvin-robot
This is an incredibly simplified wrapper for the Lego Mindstorm ev3dev project. The purpose of this wrapper is to help beginning programmers understand syntax of programming while also applying it to something physical that they can play with using the Mindstorm robots.

## Setup
- Follow the [documentation that I've created here.](https://docs.google.com/document/d/1cj98JHj5M_i-QrvKaLd5K82HGd4Qhz4xW53OiZgttpE/edit#heading=h.pn6cqlpvu8bl) 

### Available Commands
More coming soon!

\# Will print to your Lego Mindstorm's screen

marvin.print_to_screen("Put whatever you want inside these quotes!")

\# Will use the Mindstorm's microphone to speak

marvin.speak("Put whatever you want inside these quotes!")

\# Moves the robot forward. Default is 3 seconds

marvin.move_forward()

\# Moves the robot backwards. Default is 3 seconds
marvin.move_backward()

#### Gripper Specific Commands

\# Closes the gripper's claws

marvin.close_hands()

\# Opens the gripper's claws

marvin.open_hands()

## Examples:
There is sample code in robot.py. 

The following 4 lines will move the mindstorm robot forward, have it say 
"Hello world" and then move back to it's original starting point. 
The purpose here is to demonstrate what programming can do, while doing so 
in as few lines as possible. 

marvin = Marvin()

marvin.moveForward(7, 7)

marvin.speak("Hello world!")

marvin.moveBackward(7,7)

## Recent Features
- Marvin will speak to you and write out to the screen with a simple command for each
- Opening and closing the grippers works pretty well
- Turning should now work for 90 degree turns.
- Moving now uses the same functions, just works based off of motor

## TODO - Tasks that I'm still working on
- Update the marvin.py commands to all have default values
- Write more documentation on available commands
- Add a wait command
- Probably will need to create a few more classes and have more of an inheritance
structure setup as we add commands for the other mindstorms.
- Get turning working for specific degree rotations based on user input
- Figure out how to connect via bluetooth or wifi
- Marvin junior still needs ample work ensuring it matches up with Marvin, but priority right now is
marvin Sr.
- Figure out shoot-ball functionality
- Figure out sensor functionality
- Dream goal: implement some kind of AI algorithm to look around. Unsupervised learning
of course though.

## Current Bugs
- I believe the motor on my mindstorm is doing something weird. Motor b and c
do not seem to be working the same. If you use this code, your turning will not function
properly as the code currently was setup for my probably broken mindstorm

- Some commands may get skipped if they are long. I need to figure out a better method of waiting
for a command to finish as it seems like there are issues with the script trying
to run the next step before the previous one finishes

## Notes and Credit
Python naming conventions - https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7

Python encapsulation - https://medium.com/@manjuladube/encapsulation-abstraction-35999b0a3911

Turtle docs - https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.title

python ev3dev docs - https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/motors.html#medium-ev3-motor

Marvin junior voice commands - https://pyttsx3.readthedocs.io/en/latest/engine.html#examples
    sudo apt-get install espeak
