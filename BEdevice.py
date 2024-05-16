import pyautogui
import time
import subprocess
import os
import psutil
from dotenv import load_dotenv




load_dotenv()
LAUNCHER_PATH = os.getenv("LAUNCHER_PATH")
PROCESS_NAME = os.getenv("PROCESS_NAME")
# CONFIG SETTINGS
LOAD_TIME = 100 # time it takes to startup Bleeding Edge
LOGIN_TIME = 40 # time it takes to connect to Bleeding Edge server
TIME_LIMIT = 180 # time spent in waiting in queue


def is_online():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == PROCESS_NAME:
            return True
    return False

def quit_game():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == PROCESS_NAME:
            process.kill()


def join_game(code: str):
    if not is_online():
        __run_command(LAUNCHER_PATH)
        time.sleep(LOAD_TIME)
        pyautogui.press('enter')
        time.sleep(LOGIN_TIME)

    for _ in range(6):
        pyautogui.press('down')
        time.sleep(0.2)

    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('backspace')
    __write(code)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


def queue_expire():
    time.sleep(TIME_LIMIT)
    quit_game()

def enter_sleep():
    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    
def __write(message):
    pyautogui.typewrite(message=message)

def __run_command(command) -> bool:
    result = subprocess.run(command, shell=True)
    return result.returncode == 0