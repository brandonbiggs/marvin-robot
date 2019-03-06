---
layout: default
title: Recent Updates
nav_order: 5
---

## Recent Features
### March 6th Update
- Documentation has been moved from Google Doc to this site and has been expanded significantly. Hopefully things will be a bit easier from here on out.
- There are now 5 classes, 3 of which are important.
   - Robot() this class is the base class that the rest inherit from. This controls all of the functionality that all the robots will have such as screen and speaker.
   - Gripper() this is the class I was calling Marvin, but I wanted to make it less confusing, so I'm calling the class based on the type of Robot that it is. This inherits from Robot and has additional functionality of the gripper controls
   - Everstorm() this is the class I was calling Optimus. Same reason for the change as Marvin to Gripper. Simplicity.
   - Marvin() this class doesn't do anything except for inherit from Gripper(). So you can create either Gripper or Marvin and they should do the same exact things.
   - Optimus() same as Marvin. Inherits from Everstorm but nothing additional. Just a creation of the same class with a different name, just in case someone still wants to call it this.
### February Update
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
