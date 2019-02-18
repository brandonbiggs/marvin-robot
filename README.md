# MindStorm-Robot-Wrapper
This is an incredibly simplified wrapper for the 
Lego Mindstorm ev3dev project. The purpose of this wrapper is 
to help beginning programmers understand syntax of programming 
while also applying it to something physical that they can play 
with using the Mindstorm robots. Currently applicable to the 
Ev3rstorm and Gripp3r Mindstorms, which we call Optimus and Marvin
respectively.

## Setup
Follow the [documentation that I've created here.](https://docs.google.com/document/d/1WuTqk7fjde5Rwf2bOF8vLoq1V6aUO0KrKUS8NC2bF5w/edit#heading=h.316sdw9ig3yl) 

### Available Commands
More coming soon!

##### Print to your Lego Mindstorm's screen

print_to_screen("Put whatever you want inside these quotes!")

##### Use the Mindstorm's microphone to speak

speak("Put whatever you want inside these quotes!")

##### Move the robot forward. Default is 3 seconds

move_forward()

##### Moves the robot backwards. Default is 3 seconds

move_backward()

##### Have the robot wait. Default is 5 seconds

wait()

### Gripp3r Specific Commands

##### Closes the gripper's claws

marvin.close_hands()

##### Opens the gripper's claws

marvin.open_hands()

### Ev3rStorm Specific Commands

None yet

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
- Refactored wrapper to have default robot class that has the universal
commands for the Mindstorms. Marvin inherits from this class
- Added a class for the Ev3rstorms. I'm calling this "Optimus"
- Every command using either Marvin or Optimus has a default value, except turn, which requires
at least a left or right direction
- wait command has been added. Default wait is 5 seconds
- Marvin will speak to you and write out to the screen with a simple command for each
- Opening and closing the grippers works pretty well
- Turning should now work for 90 degree turns.
- Moving now uses the same functions, just works based off of motor

## TODO - Tasks that I'm still working on
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
