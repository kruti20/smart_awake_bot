import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
from src.activity_simulator import simulate_activity, stop_activity
from src.logger import logger


def create_icon():

    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill="white")

    return image


def start(icon, item):

    logger.info("Start clicked from tray")

    thread = threading.Thread(
        target=simulate_activity,
        args=(300,),
        daemon=True
    )

    thread.start()


def stop(icon, item):

    logger.info("Stop clicked from tray")

    stop_activity()


def exit_app(icon, item):

    logger.info("Application exiting")

    stop_activity()
    icon.stop()


def run_tray():

    menu = Menu(
        MenuItem("Start", start),
        MenuItem("Stop", stop),
        MenuItem("Exit", exit_app)
    )

    icon = Icon(
        "Smart Awake Bot",
        create_icon(),
        "Smart Awake Bot",
        menu
    )

    icon.run()