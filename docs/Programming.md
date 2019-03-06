---
layout: default
title: Programming the Mindstorms
nav_order: 3
---
## Programming the Mindstorms
It’s time to start programming the Lego Mindstorm Robots. Please make sure you’ve got your computer setup with Visual Studio Code, and your Lego Mindstorm is configured properly with a MicroSD card and the ev3dev linux image before you follow these 
instructions.

1. **Turn on the robot**. Turn on the mindstorm robot by pressing the center button

2. Get the code. Download our [Marvin ev3 wrapper](https://github.com/brandonbiggs/marvin-robot/blob/master/marvin-wrapper.zip) from Github
   * This will take you straight to the zip file that you can use without anything else. You’re welcome to download the rest of the project, but most if it will be very unnecessary.

3. Unpackage the code. Unzip the “marvin-wrapper.zip” folder that you just downloaded.
   * This can usually be done by right clicking and pressing “unzip” or “extract”. It changes depending on what operating system you’re using.
   * If you are unable to find a method to unzip/extract the folder, download and install the [program "7Zip"](https://www.7-zip.org/) that should make it very easy for you, and will give you a new 7zip option when you right click on the zipped folder

4. Open the code. Open Visual Studio Code, click “File” in the upper right hand corner, and then click “Open folder” from the new dropdown. You should then find and open the “marvin-wrapper” folder.
   * You should now see a file called “robot.py” and a folder called “modules”. “Robot.py” is what we care about editing and where our code will go for making the Mindstorms run. Modules is just some code that helps robot.py work.

5. Connect to the robot. Connect the mindstorm to your computer via USB, bluetooth, or wifi.
   * If you are using USB to connect your mindstorm to your computer, you don’t need to do any configuring on the robot. USB is the easiest, but least flexible method of connecting.
   * If you are connecting via bluetooth or wifi, you may have to change some options on the mindstorm. Follow the [documentation here](https://www.ev3dev.org/docs/tutorials/) for further assistance with this option.

6. Go to Settings in the bottom left corner and press “Command Palette” and type “Explore: Focus on ev3dev device browser view”. This will make a new window appear in the bottom left corner. It should look like this, except it will “Click here to connect to a device.

   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/programming-bots1.png
       "Display of EV3 Device Browser")

7. Press “Click here to connect to a device” and the search bar should appear. If you are connecting the mindstorm to your computer via USB, it may appear as “Ethernet”.

8. Once you have connected, you will now see this in the device browse

   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/programming-bots1.png
       "Display of EV3 Device Browser")

9. Hover your mouse over EV3DEV Device Browser grey title bar and click the “send project to device” button. It looks like a download button. This should take just a second. This is transferring files from your computer to the Mindstorm robot. You will get a confirmation in the bottom left once it’s completed.

10. Once you’ve gotten confirmation that the files have been transferred to your mindstorm, on your mindstorm, click on browse files, and then press enter on “robot.py”. This will start the execution of the program that you see in “robot.py” on your computer!

11. Once you can execute your program on your Mindstorm, you can now edit “robot.py” to change what your mindstorm will do. After making changes, repeat steps 9-11. Good luck!