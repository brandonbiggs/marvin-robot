## Examples:
There is sample code in robot.py. 

The following 4 lines will move the mindstorm robot forward, have it say 
"Hello world" and then move back to it's original starting point. 
The purpose here is to demonstrate what programming can do, while doing so 
in as few lines as possible. 

```
marvin = Marvin()
marvin.moveForward(7, 7)
marvin.speak("Hello world!")
marvin.moveBackward(7,7)
```