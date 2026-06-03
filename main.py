from src.gui import AwakeGUI
from src.tray import run_tray
from src.logger import logger

if __name__ == "__main__":
    logger.info("Smart Awake Bot started")
    #app = AwakeGUI()
    #app.run()
    
    run_tray()