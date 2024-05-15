# README

## Name
Bleeding Edge fill bot

## Description
A custom program to remotely execute Bleeding edge, join a custom lobby and leave

## Setup
1. Paste your discord token in .env file
2. Paste the launcher path 

## Token Aquisition
1. go to https://discord.com/developers/applications
2. click New Application
3. name it <your user> fill bot
4. accept terms
5. click 'create'
6. at the left side click bot 
7. click 'reset token'
8. click 'yes do it'
9. click copy and paste that as your disocrd_token in the .env file
10. toggle on the three privilaged gateway intents
11. click 'OAuth2' 
12. go to URL Generator
13. select bot, applications.commands
14. give permsion to Send Messages, Read Message History
15. click 'copy'
16. save that somewhere for later

## Finding launcher path
1. open file explore
2. naviage to Bleeding Edge
3. find launch_game.exe under content folder
4. right click on it and select copy as file path
5. paste that in the .env file in LAUNCHER_PATH

to get process name...
1. open bleeding edge
2. naviage to the menu
3. press ctrl + shift + esc to bring up task manager
4. click the > near bleeding edge to expand it
5. right click on the bleeding edge that is now visable
6. click properties
7. Copy the name at the top of general
8. paste this into your .env file as PROCESS_NAME

now that the .env file is set up paste the link into the discord server



## auto run
first set up bat file
1. press win key and type: where python
2. copy result into <your path> and remove the last \python.exe
3. in file explore find the fill bot folder
4. right click and select copy as path
5. paste that in both <your python path>
keep \bot.py to the end of line 4
to verify it works copy botRunner.bat as filepath and run it in terminal(win button search cmd and paste)


1. Open Task Scheduler.
2. Click "Create Task" at right side
3. Name it 5MinWakeup
4. click configure for and select windows 10

*if you have to log in from sleep mode and are putting device to sleep*
5. select run wheter user is logged on or not
6. select do not store paswords

7. click triggers at the top
8. click new
9. select daily at top left
10. set start time to be 6:00:00 PM  (us eastern convert to your time)
11. select Repeat task every: and set it to 1 minute
12. click for a duration of and set it to  9 hours
13. click ok
14. click actions at the top
15. click new
16. open file explore and find the botRunner.bat file
16. select copy as path
17. paste it under programs/script
18. click ok
19. go to settings at top
20. at the bottom of setings click on if the task is already running option
21. select Queue a new instance

*if you want your computer to be in sleep mode when not running this*
22. go to conditions select wake the computer to run this task 
23. click ok

to verify
1. open task scheduler library look for 5MinWakeup

ideas on how to lower powerdraw
lower resolution
lower brightness
lower BE settings
close unecessary applications
use plain black background
disable volume
turn off bluetooth
Disable Unused Ports:
power saver in power plan
disable non esential apps in background
