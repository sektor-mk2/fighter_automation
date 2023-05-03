# Introduction
This project automates inputs in any fighting game on PC. The user presses, for example, Forward and Low Punch and the game performs something a lot more complex and cumbersome to memorize
# How to Use
- You need to install 2 free tools - [python](https://www.python.org/downloads/) and [autohotkey](https://www.autohotkey.com/)
- Clone this repository (obviously)
- In input folder you need to put configuration text files. These files contain the key sequences to be automated. Their syntax needs a bit of explamation, so I will do it in detail in the next section.
- Run main.py, for each file in input folder it will produce an ahk file in the output folder. You can read them, if interested, but they have some complexities, the user is not expected to understand them.
- Activate any of the output files with autohotkey. While a file is being run by autohotkey, its commands will be automated
- in Input for this repo, you will find examples I use myself
# Configuration Syntax In Short
- Each line in a configuration file is a command to be automated. Here I will explain the syntax with simple examples
- fp=f,f,b+fp means "press Front Punch to automate Forward, Forward, Back + Front Punch"
- Shift+bk=d,b,f+bk means "press Shift and Back Kick to automate Down, Back, Forward and Back Kick"
- fk=u,fk means "press Front Kick to automate Up, then Front Kick"
- In examples above we used fp and bk and direction keys. You can define any key you like. Those keys are defined in CONTROLS structure and you need to rewrite it for your game
# Left and Right
- In fighting games your character can face left or right. So forward can be your left or right key, but the tool does not know which. So when you execute an automated command, you also need to press left or right. The direction you press is considered "forward" by the tool and the command is adjusted accordingly
- Example - this means that fp=f,f,b+fp really means "press your current Forward and Front Punch to automate ..."
# Configuration Syntax In Detail
- The following section explains the configuration in more formal detial
- Each line in a configuration file is expected to be 1 of 3 things - empty line, a comment or a command to be automated
- comments start with ;
- comments and empty lines are preserved in the output file
- commands are the main thing
- commands have the following format - "modifier+key=key,key, ... key + key + key
- left hand side can start with a modifier. Modifiers are optional. Currently supported modifiers are Ctrl, Alt, Shift
- right hand side has sequences of keys, separated with commas. Commas mean "pres this after that". Sequence is of arbitrary length.
- sequences in right hand side can have pluses. Plusses mean "press in the same time"
- keys are not keyboard keys but game keys. For example f means Forward, b means Backward, bp may mean Back Punch
- keys are defined in CONTROLS structure
# License
This project is free unless you are an asshole
# Next Versions
In the future I need to extract CONTROLS in proper config and also variables for key hold time and delay between key presses, Defaults work fine for what games I play but it may be useful