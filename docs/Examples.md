---
layout: default
title: Examples
nav_order: 5
---

## Examples:
There is other sample code in examples.py. 

The following 5 lines will move the mindstorm robot forward, have it say 
"Hello world" and then move back to it's original starting point. 

```
from modules.robot import *
robot = Robot()
robot.moveForward(7, 7)
robot.speak("Hello world!")
robot.moveBackward(7,7)
```