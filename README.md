# README

## Name
Bleeding Edge fill bot

## Description
A custom program to remotely execute Bleeding edge, join a custom lobby and leave

## Setup
### Create New Discord Bot
1. Go to https://discord.com/developers/applications
2. Select New Application
3. Name it \<your user\> fill bot
4. Chcek the check-box to accept Discord's TOS
5. Select 'Create'

### Configure Bot Settings
1. Select 'Bot' in settings  
2. Make sure the three privilaged gateway intents are on
3. Check the 'Administator' permission under 'Bot Permissions'
4. In the .env file, paste the token at \<disocrd_token\>
5. Navigate back to the discord developer portal
6. Select 'OAuth2' 
7. Under 'OAuth2 URL Generator' check 'bot' & 'applications.commands'
8. Under 'Bot Permisions' check 'Send Messages' & 'Read Message History'

### Paste Bot Token Into .env File
In the discord developer portal...
1. Select 'Bot' in settings
2. Select 'Reset Token'
3. Select 'Yes, do it!'
4. Select 'Copy'

### Add Bot to server.
> [!IMPORTANT]
> In order to add the bot to a server an admin of the server must accept the bot
1. Select 'OAuth2'
2. Under 'Generated URL' select 'copy'
3. save that somewhere for later


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
