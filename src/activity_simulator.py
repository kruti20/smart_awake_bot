import pyautogui
import time
import random
from src.logger import logger

running = False

def simulate_activity(interval):
    global running
    running = True

    logger.info("Activity simulation started")

    while running:
        action = random.choice(["move", "scroll", "key"])
        random_mouse_move()
        pyautogui.press('capslock')    

        print("Simulated activity")
        logger.info("Simulated mouse and keyboard activity")

        time.sleep(interval)

def stop_activity():
    global running
    print("Stopped activity")
    running = False
    logger.info("Activity simulation stopped")


def random_mouse_move():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    duration = random.uniform(0.5, 2.5)
    pyautogui.moveRel(x, y, duration=duration)
    #pyautogui.click(x, y)


def random_scroll():
    pyautogui.scroll(random.randint(-500, 500))

def random_key():
    keys = ['shift', 'ctrl', 'alt']
    pyautogui.press(random.choice(keys))