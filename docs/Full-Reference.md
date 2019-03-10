---
layout: default
title: Full Reference
nav_order: 4
---
# Full Reference

This reference list should provide you with fully executable examples of how to use each command to control your Lego Mindstorm. 

- You **do not** need to use the `from modules.robot import *` command after each script. That will only need to be used once at the top of your file. The same can be said for your creation of robot with the line `robot = Robot()`. 
- **Do not** copy the line that starts with `#>` in the examples. That is just an example of what is output after the commands are ran.
- Each robot can execute all of the commands **not** listed in the specific robot command section. Example - The Ev3rstorm cannot use the Gripp3r commands to open or close hands. But both can use `print_to_screen` or `speak`.

### Table of Contents
**[Print](#print)**<br>
**[Speak](#speak)**<br>
**[Move Forward](#move-forward)**<br>
**[Move Backward](#moves-backward)**<br>
**[Wait](#wait)**<br>
**[Gripp3r Specific](#gripp3r-specific-commands)**<br>
**[Ev3rstorm Specific](#ev3rstorm-specific-commands)**<br>

### Class Instantiation
Todo - Document the instantiation

### Print
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

### Set Volume
You can change the speaker volume of the Lego Mindstorm. The volume is a percent between 0 and 100 where 0 is no sound and 100 is max. By default, this command will set the volume at 80%. The volume is not very loud on these, so 100% isn't too terrible to hear.
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

### Move Forward
TODO - This will be improved soon
```
from modules.robot import *
robot = Robot()
robot.move_forward()
```

### Moves Backward
TODO - This will be improved soon
```
from modules.robot import *
robot = Robot()
robot.move_backward()
```

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
### Write Song
TODO

### Write Tune
TODO

### Play Random Song
The difference between a song and a tune is with how each is produced by the robot. See section on writing tones and writing songs for more information on the differences.

The robot has the ability to play a song using a series of beeps. There are several predefined songs that have been written already for you. To select a random song, use this command, with length being set to either `short` or `long`. The short parameter will play a relatively short song, while the long parameter will play a slightly longer song.
```
from modules.robot import *
robot = Robot()
robot.sing_random_song(length="short")
#> Random song will be selected and played
```

### Play Tone
The difference between a song and a tune is with how each is produced by the robot. See section on writing tones and writing songs for more information on the differences.

The robot has the ability to play a random tune using a series of different sounding tunes. There are several predefined tunes that have been written already for you.



## Gripp3r Specific Commands
These commands can only be run on the Gripp3r Lego Mindstorm.

### Close Gripp3r Claws
This will close the Gripp3r's claws and move the claws upward, lifting
the object slightly off the ground.
```
from modules.robot import *
robot = Robot()
gripper = Gripper()
gripper.close_hands()
```

### Open Gripp3r Claws
This will open the Gripp3r's claws and lower them to the base of the robot.
```
from modules.robot import *
robot = Robot()
gripper = Gripper()
gripper.open_hands()
```

## Ev3rStorm Specific Commands
Coming soon
{: .label .label-yellow }