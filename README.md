# README

## Name
Bleeding Edge fill bot

## Description
- A python script to remotely execute Bleeding Edge, join a custom games lobby, and exit.
- A bat script to ensure the python file runs correctly when ran by task scheduler

## How to use
use the join command to specify what lobby code the bot should join
run the bot script (either automatically or manually) to execute the actions

### Commands
- !join [code]: Launches Bleeding Edge and Queues for the specified code

## Setup Bot
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
4. In the .env file, paste the token at \<disocrd token\>
5. Navigate back to the discord developer portal
6. Select 'OAuth2' 
7. Under 'OAuth2 URL Generator' check 'bot' & 'applications.commands'
8. Under 'Bot Permisions' check 'Send Messages' & 'Read Message History'

### Paste The Discord Token Into .env File
In the discord developer portal...
1. Select 'Bot' in settings
2. Select 'Reset Token'
3. Select 'Yes, do it!'
4. Select 'Copy'
5. In the .env file, paste the token at \<discord token\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Add The Bot To Server.
> [!IMPORTANT]
> To add the bot to a server, an admin of the server must authorize the bot
1. Select 'OAuth2'
2. Under 'Generated URL' select 'copy'
3. Paste the link into a channel of the server
4. To authorize, click the link and select 'Authorize'

### Paste The Game's launcher Path Into .env File
1. Open file explore
2. Naviage to Bleeding Edge directory
3. Locate 'launch_game.exe' in Bleeding Eduge > Content > launch_game.exe
4. right click on 'launch_game.exe' and select 'Copy as path'
5. In the .env file, paste the path at \<launcher path\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Paste The Process Name Into .env FIle
1. Open Bleeding Edge
2. Naviage to the menu of the game
3. Press ctrl + shift + esc to bring up task manager
4. Locate Bleeding Edge in the process list.
> ![NOTE]
> The process can sometimes be listed as MobladeClient...exe. If that is the case copy that name into the .env file
5. Select the > to the left of Bleeding Edge to expand
6. Right click the process under Bleeding Edge
7. Select 'properties' 
8. Copy the name of the process
9. In the .env file, paste the process name at \<process name\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Paste Your Bot Channel ID
> [!NOTE]
> skip to step 4 if your account already has developer mode enabled
1. open Discord
2. go to Settings > Advanced
3. enable developer mode
4. right-click on the channel you want the bot to monitor
5. select 'Copy ID'
6. In the .env file, paste the process name at \<channel id\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

## Setup Task Scheduler 
If you want the program to run automatically follow these steps

### Paste The Path Into The Bot Runner File
1. Open command prompt
2. Enter the command "where python"
3. copy the result into \<path\> and remove "\python.exe"
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Paste The Python  
5. in file explore find the fill bot folder
6. right click and select copy as path
7. paste that in both <your python path>
keep \bot.py to the end of line 4
to verify it works copy botRunner.bat as filepath and run it in terminal(win button search cmd and paste)
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

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

## Additional configuration

## Ways to reduce powerdraw device

