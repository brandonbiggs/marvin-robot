---
layout: default
title: Getting Started
nav_order: 2
---
# Setup
## Table of Contents
**[Contact Us](#contact-us)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Windows Setup](#windows-setup)**<br>
**[Mac Setup](#mac-setup)**<br>
**[Linux Setup](#linux-setup)**<br>
**[ChromeOS Setup](#chromeos-setup)**<br>
**[Configuration](#configuration)**<br>
**[Programming](#programming-the-mindstorms)**<br>
**[Helpful Resources](#helpful-resources)**<br>

## Contact Us
Visit Idaho State University’s [Computer Science Program](https://www.isu.edu/cs/) or our [outreach website](https://www2.cose.isu.edu/~bodipaul/outreach/).

Visit [Dr. Paul Bodily’s](https://www2.cose.isu.edu/~bodipaul/) Academic Website

This documentation was put together by [Brandon Biggs](mailto:biggbran@isu.edu), Katie Wilsdon, and [Dr. Bodily](mailto:bodipaul@isu.edu).

## Prerequisites
1. Computer with an internet connection for installing and configuring several pieces of software
2. [EV3 Lego Mindstorm Robot](https://wwwsecure.eu.lego.com/en-us/mindstorms/build-a-robot)  
   * Currently we have tested this with the Gripp3r and Ev3rstorm
3. MicroSD Card that is not bigger than 32GBs

## Windows Setup
1. Download and install [Python 3.7.2](https://www.python.org/downloads/)
   * Windows x86-64 executable installer
2. Download and install [Visual Studio Code](https://code.visualstudio.com/download)
   * Visual Studio Code is a free code editor from microsoft. It’s like notepad but more powerful
   * This set up to allow programming with the Lego Mindstorm Robots. Any code editor will actually work, but this has a very helpful extension

3. After Visual Studio Code is installed, open the program and click on “settings”, which is just an icon located in the bottom left corner, picture below.

   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup1.png)
       "Visual Studio Code Main Menu"

4. Type “python” in the search bar and then click Python. It is the top link in this photo. Press “install”. It will be in the same location as “uninstall” in this photo.
    ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup2.png
       "Visual Studio Code Main Menu" )

5. There should be a button that appears. You need to click “reload” to activate Python.

6. Next we need to set the Python interpreter
   * Click the Settings Icon at the bottom of the left panel
   * Click command palette
   
   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup3.png
       "Visual Studio Code Main Menu" )

   * A search box should appear. Type Python and select “Python: Select Interpreter”
   
   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup4.png
       "Visual Studio Code Main Menu" )
   
   * After you select “Python: Select Interpreter”, it should have another link that says “Python 3.7.2”. Click this as that is what we just installed in step 1.

7. A box in the right hand corner should pop up called Python Linting. Click Install.

8. This terminal should pop up at the bottom of the screen

   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup5.png
       "Visual Studio Code Main Menu" )

9. Next we need to install the EV3Dev-browser. This extension will allow us to interact directly with the Lego mindstorm robot

   * Click on “settings”, which is just an icon located in the bottom left corner, picture below.
 
   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup6.png
       "Visual Studio Code Main Menu")
 
   * In the search bar, type “ev3dev-browser”. You should now be able to install it. It looks like this
   
   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup7.png
       "Visual Studio Code Main Menu")
   
   * You will be prompted to reload after you press install. You should do this.

10. We now need to check a few other settings in Visual Studio Code

    * First, we need to check that the line endings are set properly.

      - Open settings in the bottom left corner, click “Settings”

      - Type in the search bar “line end” and make sure that the top setting “Files: EOL” is set to “\n” pictured below.
    
    ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup8.png
       "Visual Studio Code Main Menu" )

11. We should now done configuring your Windows computer for programming the Lego Mindstorm Robots!

## Mac Setup
1. Download and install [Python 3.7.2](https://www.python.org/downloads/release/python-372/) 

   * You’ll want the macOS 64-bit installer

2. Download and install [Visual Studio Code](https://code.visualstudio.com/download)

3. Follow the Windows instructions for installing and configuring Visual Studio Code

## Linux Setup
1. Install Python3 by using your favorite package manager or directly from the Python website

2. Follow the Windows instructions for installing and configuring Visual Studio Code. Like mentioned in those instructions, you don’t have to use VS Code, we just recommend it since it has the nice ev3dev-browser extension.

## ChromeOS Setup
This hasn’t been tested, but should technically be possible with the newer chromebooks that have linux support with Crostini. If you would like to approach setting up everything to work with a chromebook, please email [biggbran@isu.edu](mailto:biggbran@isu.edu) and we can talk about how this might be possible.

## Configuration
We have one more set of instructions before we can start programming the Lego Mindstorm Robots. We must configure our robots to allow for Python programming to work on them.
1. Follow the [official documentation](https://www.ev3dev.org/docs/getting-started/#step-2-flash-the-sd-card) for installing the EV3dev image on a MicroSD card. You only need to follow steps 1-4. Any further than that may be helpful, but isn’t necessary

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

### Helpful Resources
* You may find many different tutorials out there. The only thing that we change from most tutorials is that we use a custom Python programming wrapper to make programming the Lego Mindstorms much easier. Experienced programmers should be able to use any code tutorials out there, we just recommend ours to help even the most inexperienced programmers.

* List of all available commands that can be ran using our wrapper can be found on the Github readme page

* Visual Studio Code won’t open unless connected to the internet - [Solution](https://github.com/Microsoft/vscode/issues/7570#issuecomment-454806257)

* [Ev3dev website](https://www.ev3dev.org/docs/getting-started/) 

* Set up your Lego EV3 robot and your [computer tutorial](https://sites.google.com/site/ev3python/setting-up-vs-code)

* [General Troubleshooting](https://sites.google.com/site/ev3python/troubleshoot) 

* [Selecting a python interpreter](https://code.visualstudio.com/docs/python/environments) 

* [Ev3dev-browser information](https://marketplace.visualstudio.com/items?itemName=dlech.ev3dev-browser)