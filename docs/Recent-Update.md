---
layout: default
title: Recent Updates
nav_order: 5
---

## Recent Features and Patch Notes

### March 10th Update
- I thought March 9th's update was big. This one doesn't implement as many new features, but was very important for a lot of reasons below.
- Moving forward, backward, and turning are all now based on distance and rotation of the motor rather than time. I tested these a fair amount. There's still more testing to be done, but they seem to be working really well. Not perfect, but a lot better than my poor implementation of time based movement and turning.
- TONS of code documentation and cleanup. I read a lot about python code documentation. Hopefully the comments here are a little more 'correct'. With these changes, you can now use the `.__doc__` functionality. I don't know a ton about this, I just read that it was the more correct way to document code.
- Cleaned up a couple of things with the features I implemented yesterday.

### March 9th Update
- Absolutely gigantic update
- Lots and lots of error checking in the code. Hopefully this removes most of the bugs that people may have had. Combining these changes along with the Python syntax checking, things should be in good shape in terms of possible bugs. This isn't the case for movement just yet, but we're working on that. Should have an update for that tomorrow.
- New Features! Beeping, songs, tunes, LEDs, volume control are all now available. See "full-reference" for more information about all of these.
- Unit testing is in the works. I've never really implemented unit testing before, so it could be really wrong. Feel free to laugh, but let me know how I can improve it.
- Documentation updates - not just with new features. Updated documentation to go along with old features as well.
- Debug Mode! You can now pass a parameter on init of robot to enter debug mode. This will print lots of output on the computer when attempting to run commands. Don't run this on the robots however.
- Movement updates coming soon. I've made lots of progress on this, even if the code doesn't reflect it yet. I believe I know how to get turning and distance moving setup quite nicely.

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
