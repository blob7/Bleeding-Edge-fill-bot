# README

## Name
Bleeding Edge fill bot

## Description
A script to remotely execute Bleeding Edge, join a custom games lobby, and exit from a discord command.

## How to use
use the join command to specify what lobby code the bot should join
run the bot script (either automatically or manually) to execute the actions

### Discord Commands
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
> [!NOTE]
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
1. Open Discord
2. Go to Settings > Advanced
3. Enable developer mode
4. Right-click on the channel you want the bot to monitor
5. Select 'Copy ID'
6. In the .env file, paste the process name at \<channel id\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

## Setup Task Scheduler 
If you want the program to run automatically follow these steps
The purpose of the bat file is to ensure the task scheduler runs the file correctly

### Paste Python's Path Into The Bot Runner File
1. Open command prompt
2. Enter the command "where python"
3. Copy the result
> [!NOTE]
> If you see multiple results, select the first one
4. In the Bot Runner file, paste the path at \<path\> and remove "\python.exe"
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Paste The Bot Directory Into The Bot Runner File
1. Open file explorer
2. Navigate to your fill bot folder
3. Right click and select copy as path
4. Paste the directory path in both \<dir path\>
> [!IMPORTANT]
> Remove the "\<" "\>" when your enter your information

### Configure The Task.
1. Copy the directory path from the previous step
2. Open the 10MinFillBot.xml in a text editor
3. In the command tags replace "your_dir" with the directory

### Import The Task
1. Open Task Scheduler
2. *Optional*: create a new folder called My Tasks
3.  Select 'Import Task...'
4.  Select 10MinFillBot.xml
5.  Select 'OK'

## Additional configuration
### Automatic sleep mode when not checking 
1. Open Task Scheduler
2. Select 10MinFillBot
3. Select 'Properties'
4. Select 'Conditions'
5. Select 'Wake the computer to run this task'
6. Select 'OK'
7. Open the .env file
8. Set DO_SLEEP to equal to True

## Ways to reduce powerdraw device
- Lower resolution
- Lower brightness
- Lower BE settings
- Close unecessary applications
- Use plain black background
- Disable volume
- Turn off bluetooth
- Disable Unused Ports:
- Power saver in power plan
- Disable non esential apps in background
