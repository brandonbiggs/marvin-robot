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
