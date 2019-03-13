---
layout: default
title: Full Reference
nav_order: 4
---
# Full Reference
## Table of Contents
### General
**[General Information](#general-information)**<br>
**[Class Instantiation](#class-instantiation)**<br>
**[Function Information](#function-information)**<br>
**[Print to Screen](#print-to-screen)**<br>
**[Buttons](#button-colors)**<br>
**[Wait](#wait)**<br>

___

### Movement Control
**[Move Forward](#move-forward)**<br>
**[Move Backward](#moves-backward)**<br>
**[Turning](#turning)**<br>

___
### Sounds
**[Beep](#beep)**<br>
**[Set Volume](#set-volume)**<br>
**[Speak](#speak)**<br>
**[Play Random Songs](#play-random-song)**<br>
**[Play Random Tones](#play-random-tone)**<br>
<!--**[Write Song - TODO](#write-song)**<br>
**[Write Tune - TODO](#write-tune)**<br>-->

___

### Gripp3r Specific
**[Close Claws](#close-claws)**<br>
**[Open Claws](#open-claws)**<br>

___
<!--### Ev3rstorm Specific
**[Ev3rstorm Specific](#ev3rstorm-specific-commands)**<br>
___
-->

### Demos
**[Baby Shark](#demo-baby-shark)**<br>
**[Race Car](#demo-racecar)**<br>
**[Dance](#demo-dance)**<br>
**[Silly Sounds](#demo-play-sound)**<br>


### General Information
This reference list should provide you with fully executable examples of how to use each command to control your Lego Mindstorm. 

- You **do not** need to use the `from modules.robot import *` command after each script. That will only need to be used once at the top of your file. The same can be said for your creation of robot with the line `robot = Robot()`. 
- **Do not** copy the line that starts with `#>` in the examples. That is just an example of what is output after the commands are ran.
- Each robot can execute all of the commands **not** listed in the specific robot command section. Example - The Ev3rstorm cannot use the Gripp3r commands to open or close hands. But both can use `print_to_screen` or `speak`.
- Once your robot gets to ~20% battery life, once you run a command on the robot, it will tell you that the battery is getting low. This doesn't mean you have to change the batteries, but your results may differ from that of a robot with full batteries.

___

### Class Instantiation
By default, the class is very straightforward to instantiate.
```
from modules.robot import *
robot = Robot()
#> You know have a robot object!
```

There are several parameters you can pass to it however. Right now the ones that are useful are: `left_track`, `right_track`, and `debug`. The two track parameters allow you to change the motors which your Lego Mindstorms may be using. By default `left_track` is set to "outB" and `right_track` is set to "outC". These were just the defaults for the Mindstorms we used. If your robot has them set differently, instantiate the class like the following, where `outX` and `outY` are the proper motors for each left and right track.
```
from modules.robot import *
robot = Robot(left_track="outX", right_track="outY")
#> You know have a robot object with different motors set for each track
```

You can also enable debug mode. **Do not** enable this when running code on the robot. This is useful if you are testing the code on your computer. This should allow you to run everything as you would normally with the robot, with printed output of what would happen on your computer. This allows for checking of commands and whatnot. 

```
from modules.robot import *
robot = Robot(debug=True)
#> You are now in debug mode. Commands will run on your computer, but not on the robot.
```

___

### Function Information
Every command should have an explanation command. To get this explanation, use your computer to run the following command `robot.<function_name>.__doc__`. You should get an explanation of the function. Just replace `<function_name>` with the function you want information about, excluding the parenthesis. This will not work on the robot and will only work on the computer you're programming with. Here's an example:
```
from modules.robot import *
robot = Robot()
print(robot.beep.__doc__)
```
This will print out an explanation of the `beep` function on your computer.
___

### Print to Screen
This will allow you to print to your Lego Mindstorm's screen.
The print_to_screen command does not need any parameters by default.

```
from modules.robot import *
robot = Robot()
robot.print_to_screen()
#> Hello everyone!
```

You are welcome to pass it a statement, which will be printed to the Mindstorm screen

```
from modules.robot import *
robot = Robot()
robot.print_to_screen("Put whatever you want inside these quotes!")
#> Put whatever you want inside these quotes!
```
___

### Button Colors
You can change the LED colors of two buttons on the Mindstorm controller. By default, the left button is set to be green.
```
from modules.robot import *
robot = Robot()
robot.robot.set_button_colors()
#> The left button will be set to green
```

You are able to use the following colors: 'black', 'red', 'green', 'amber', 'orange', 'yellow'. Just set the parameter to any of these colors.
 ```
from modules.robot import *
robot = Robot()
robot.robot.set_button_colors(color="orange")
#> The left button will be set to orange
```

You can specify the right button as well.
 ```
from modules.robot import *
robot = Robot()
robot.robot.set_button_colors(color="orange", button="right")
#> The right button will be set to orange
```

You may also specify a brightness percentage from 0 to 100, using the last parameter `brightness`.
 ```
from modules.robot import *
robot = Robot()
robot.robot.set_button_colors(color="orange", button="right", brightness=50)
#> The right button will be set to orange with brightness set to 50%
```
___

### Wait
This command will pause the robot for 5 seconds.
```
from modules.robot import *
robot = Robot()
robot.wait()
#> 5 second pause
```

You can increase or decrease this time by passing the number of seconds
as a parameter.
```
from modules.robot import *
robot = Robot()
robot.wait(seconds=10)
#> 10 second pause
```
___

### Move Forward
The move forward command allows the robot to move forward however many feet you want it to. There are a couple of settings to make it more powerful, but by default, the `move_forward()` command will move the robot forward one foot.
```
from modules.robot import *
robot = Robot()
robot.move_forward()
#> The robot will move forward 1 foot
```

You can change the number of feet and have the robot move forward more than a foot, but no more than 15 feet.
```
from modules.robot import *
robot = Robot()
robot.move_forward(distance_in_feet=5.5)
#> The robot will move forward 5.5 feet
```

You can also increase the speed in which your robot moves. By default, it will move at speed 3. This is the most tested speed. Any other speed may have some varied output. The speed is a number between 1 and 10.
```
from modules.robot import *
robot = Robot()
robot.move_forward(speed=7)
#> The robot will move forward 1 foot at speed 7.
```

In the initial explanation of `distance_in_feet` I specified that there is a cap of 15 feet. This is to ensure there isn't a typo from the user. If you really want the robot to move more than 15 feet in one command, use the `override=True` parameter.
```
from modules.robot import *
robot = Robot()
robot.move_forward(distance_in_feet=30, override=True)
#> The robot will move forward 30 feet at default speed.
```

This can all be put together by specifying each of the commands as parameters.
```
from modules.robot import *
robot = Robot()
robot.move_forward(distance_in_feet=30, speed=8, override=True)
#> The robot will move forward 30 feet at speed 8.
```

There is one more **very** advanced feature. This is not needed most of the time. You can specify a `surface_factor`. This is usually a small +/- integer that helps account for surface slowdown or speedup. Distance and speed were measured on a hard surface, but a carpet surface may change how far the robot is moving. If the robot isn't moving quite as far on a surface as on another surface, pass a small positive number, such as 10, to the move forward command.

```
from modules.robot import *
robot = Robot()
robot.move_forward(surface_factor=10)
#> The robot will move forward approximately 1 foot using a small surface factor.
```
___

### Moves Backward
The move backward command allows the robot to move backward however many feet you want it to. There are a couple of settings to make it more powerful, but by default, the `move_backward()` command will move the robot backward one foot.
```
from modules.robot import *
robot = Robot()
robot.move_backward()
#> The robot will move backward 1 foot
```

You can change the number of feet and have the robot move backward more than a foot, but no more than 15 feet.
```
from modules.robot import *
robot = Robot()
robot.move_backward(distance_in_feet=5.5)
#> The robot will move backward 5.5 feet
```

You can also increase the speed in which your robot moves. By default, it will move at speed 3. This is the most tested speed. Any other speed may have some varied output. The speed is a number between 1 and 10.
```
from modules.robot import *
robot = Robot()
robot.move_backward(speed=7)
#> The robot will move backward 1 foot at speed 7.
```

In the initial explanation of `distance_in_feet` I specified that there is a cap of 15 feet. This is to ensure there isn't a typo from the user. If you really want the robot to move more than 15 feet in one command, use the `override=True` parameter.
```
from modules.robot import *
robot = Robot()
robot.move_backward(distance_in_feet=30, override=True)
#> The robot will move backward 30 feet at default speed.
```

This can all be put together by specifying each of the commands as parameters.
```
from modules.robot import *
robot = Robot()
robot.move_backward(distance_in_feet=30, speed=8, override=True)
#> The robot will move backward 30 feet at speed 8.
```

There is one more **very** advanced feature. This is not needed most of the time. You can specify a `surface_factor`. This is usually a small +/- integer that helps account for surface slowdown or speedup. Distance and speed were measured on a hard surface, but a carpet surface may change how far the robot is moving. If the robot isn't moving quite as far on a surface as on another surface, pass a small positive number, such as 10, to the move forward command. If for whatever reason it's moving more than a foot, pass a small negative number. 

```
from modules.robot import *
robot = Robot()
robot.move_backward(surface_factor=10)
#> The robot will move backward approximately 1 foot using a small surface factor.
```
___

### Turning
def turn(self, direction, speed=3, degrees=90, surface_factor=0):

The robot will turn right or left, however many degrees you want it to. By default, you must pass a direction, either `direction="left"` or `direction="right"` to the `turn()` command. Both of these will turn the robot either 90 degrees to the left or right accordingly.
```
from modules.robot import *
robot = Robot()
robot.turn(direction="right")
#> The robot will turn 90 degrees to the right
```

You can update the speed in which the robot turns. The default speed is 3, and this was the most tested turning speed, but other speeds should work as well. Speed is an integer between 1 and 10.
```
from modules.robot import *
robot = Robot()
robot.turn(direction="left", speed=5)
#> The robot will turn 90 degrees to the left at speed 5
```

You can change the number of degrees your robot turns to the left or right by adding a `degrees=` parameter. This will override the 90 degree default.
```
from modules.robot import *
robot = Robot()
robot.turn(direction="right", degrees=180)
#> The robot will turn 180 degrees to the right.
```

You can combine all of these parameters.
```
from modules.robot import *
robot = Robot()
robot.turn(direction="left", degrees=180, speed=8)
#> The robot will turn 180 degrees to the left at speed 8.
```

There is one more **very** advanced feature. This is not needed most of the time. You can specify a `surface_factor`. This is usually a small +/- integer that helps account for surface slowdown or speedup. Turning was measured on a hard surface, but a carpet surface may change how far the robot turns. If the robot isn't turning quite as far on a surface as on another surface, pass a small positive number, such as 10, to the move forward command. If for whatever reason it's turning more than it should, pass a small negative number. 

```
from modules.robot import *
robot = Robot()
robot.move_turn(direction="right", surface_factor=10)
#> The robot will turn right approximately 90 degrees, but may be a bit more because of the surface factor
```
___

### Beep
The robot can beep at you with a simple command.
```
from modules.robot import *
robot = Robot()
robot.beep()
#> One beep will emit from the robots speaker
```

The number of beeps can be between 0 and 15.
```
from modules.robot import *
robot = Robot()
robot.beep(15)
#> 15 beeps will emit from the robots speaker
```

If you want more than 15 beeps, you can override the 15 beep limit. If this was a mistake, you can stop the robot by pressing the center button on the robot.
```
from modules.robot import *
robot = Robot()
robot.beep(300, override=True)
#> 300 beeps will emit from the robots speaker
```
___

### Set Volume
You can change the speaker volume of the Lego Mindstorm. The volume is a percent between 0 and 100 where 0 is no sound and 100 is max. By default, this command will set the volume at 80%. The volume is not very loud on these, so 100% isn't too terrible to hear. This only works for the speak command. Does not affect the beeps or tone commands.
```
from modules.robot import *
robot = Robot()
robot.set_volume()
#> Volume of speaker will be set to 80%
```

Set the volume to whatever you'd like.
```
from modules.robot import *
robot = Robot()
robot.set_volume(100)
#> Volume of speaker will be set to 100%
```
___

### Speak
Use this command to have your Lego Mindstorm speak to you through the 
built in speaker. The speak command does not need any parameters 
by default.

```
from modules.robot import *
robot = Robot()
robot.speak()
#> Hello. I am Marvin. Nice to meet you.
```

You are welcome to pass a statement to the speak command as well.
```
from modules.robot import *
robot = Robot()
robot.speak("Put whatever you want inside these quotes!")
#> Put whatever you want inside these quotes!
```
___

### Play Random Song
The difference between a song and a tune is with how each is produced by the robot. See section on writing tones and writing songs for more information on the differences.

The robot has the ability to play a song using a series of beeps. There are several predefined songs that have been written already for you. To select a random song, use this command, with length being set to either `short` or `long`. The short parameter will play a relatively short song, while the long parameter will play a slightly longer song.
```
from modules.robot import *
robot = Robot()
robot.sing_random_song(length="short")
#> Random song will be selected and played
```
___

### Play Random Tone
The difference between a song and a tune is with how each is produced by the robot. See section on writing tones and writing songs for more information on the differences.

The robot has the ability to play a random tune using a series of different sounding tunes. There are several predefined tunes that have been written already for you.

___

## Gripp3r Specific Commands
These commands can only be run on the Gripp3r Lego Mindstorm.

### Close Claws
This will close the Gripp3r's claws and move the claws upward, lifting
the object slightly off the ground.
```
from modules.robot import *
gripper = Gripper()
gripper.close_hands()
```
___

### Open Claws
This will open the Gripp3r's claws and lower them to the base of the robot.
```
from modules.robot import *
gripper = Gripper()
gripper.open_hands()
```

<!--
## Ev3rStorm Specific Commands
Coming soon
{: .label .label-yellow }

### Write Song
Coming soon
{: .label .label-yellow }

### Write Tune
Coming soon
{: .label .label-yellow }
-->

___

### Demo Baby Shark
Sings a short and slightly modified version of babyshark.
```
from modules.robot import *
robot = Robot()
robot.demo_babyshark()
```

___

### Demo Racecar
The robot will act as a racecar, but only moves a few inches at a time.
```
from modules.robot import *
robot = Robot()
robot.demo_racecar()
```
___

### Demo Dance
The robot will do a mini robot dance.
```
from modules.robot import *
robot = Robot()
robot.demo_dance()
```
___

### Demo Play Sound
You can play a few short sound bytes. These are different from tones and songs as this is actually using a .wav file.

You have two choices here, `name="car"` or `name="sneeze"`. 
```
from modules.robot import *
robot = Robot()
robot.demo_play_sound(name="sneeze")
#> The robot will sneeze
```