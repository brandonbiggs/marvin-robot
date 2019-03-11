---
layout: default
title: Examples
nav_order: 5
---

## Examples:
There is other sample code in examples.py. 

The following 5 lines will move the mindstorm robot forward 5 feet, have it say 
"Hello world" and then move back to it's original starting point. 

```
from modules.robot import *
robot = Robot()
robot.move_forward(distance_in_feet=5.0)
robot.speak("Hello world!")
robot.move_backward(distance_in_feet=5.0)
```