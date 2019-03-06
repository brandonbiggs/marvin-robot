---
layout: default
title: Getting Started
nav_order: 2
---
# Setup
## Table of Contents
**[Prerequisites](#prerequisites)**<br>
**[Windows Setup](#windows-setup)**<br>
**[Mac Setup](#mac-setup)**<br>
**[Linux Setup](#linux-setup)**<br>
**[ChromeOS Setup](#chromeos-setup)**<br>
**[Configuration](#configuration)**<br>
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

   ![alt text](https://raw.githubusercontent.com/brandonbiggs/marvin-robot/master/docs/images/winsetup1.png
       "Visual Studio Code Main Menu")

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