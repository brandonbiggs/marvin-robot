---
layout: default
title: Full Reference
nav_order: 3
---
# Full Reference
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
marvin = Robot()
marvin.print_to_screen()
> Hello everyone!
```

You are welcome to pass it a statement, which will be printed to the Mindstorm screen

```
marvin = Robot()
marvin.print_to_screen("Put whatever you want inside these quotes!")
> Put whatever you want inside these quotes!
```

### Speak
Use this command to have your Lego Mindstorm speak to you through the 
built in speaker. The speak command does not need any parameters 
by default.

```
marvin = Robot()
marvin.speak()
> Hello. I am Marvin. Nice to meet you.
```

You are welcome to pass a statement to the speak command as well.
```
marvin = Robot()
marvin.speak("Put whatever you want inside these quotes!")
> Put whatever you want inside these quotes!
```

### Move Forward
TODO - This will be improved soon
```
marvin = Robot()
marvin.move_forward()
```

### Moves Backward
TODO - This will be improved soon
```
marvin = Robot()
marvin.move_backward()
```

### Wait
This command will pause the robot for 5 seconds.
```
marvin = Robot()
marvin.wait()
> 5 second pause
```

You can increase or decrease this time by passing the number of seconds
as a parameter.
```
marvin = Robot()
marvin.wait(seconds=10)
> 10 second pause
```

## Gripp3r Specific Commands

### Close Gripp3r Claws
This will close the Gripp3r's claws and move the claws upward, lifting
the object slightly off the ground.
```
marvin = Robot()
marvin.close_hands()
```

### Open Gripp3r Claws
This will open the Gripp3r's claws and lower them to the base of the robot.
```
marvin = Robot()
marvin.open_hands()
```

## Ev3rStorm Specific Commands

None yet