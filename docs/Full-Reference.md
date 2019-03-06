---
layout: default
title: Full Reference
nav_order: 4
---
# Full Reference

This reference list should provide you with fully runnable examples of how to use each command to control your Lego Mindstorm. 

- You **do not** need to use the `from modules.robot import*` command after each script. That will only need to be used once at the top of your file. The same can be said for your creation of robot with the line `robot = Robot()`. 
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