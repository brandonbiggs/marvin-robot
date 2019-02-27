---
layout: default
title: Future Work
nav_order: 6
---

## TODO - Tasks that I'm still working on
- Get turning working for specific degree rotations based on user input
- Figure out how to connect via bluetooth or wifi
- Marvin junior still needs ample work ensuring it matches up with Marvin, but priority right now is
marvin Sr.
- Figure out shoot-ball functionality
- Figure out sensor functionality
- Dream goal: implement some kind of AI algorithm to look around. Unsupervised learning
of course though.

## Current Bugs
- I believe the motor on my mindstorm is doing something weird. Motor b and c
do not seem to be working the same. If you use this code, your turning will not function
properly as the code currently was setup for my probably broken mindstorm

- Some commands may get skipped if they are long. I need to figure out a better method of waiting
for a command to finish as it seems like there are issues with the script trying
to run the next step before the previous one finishes