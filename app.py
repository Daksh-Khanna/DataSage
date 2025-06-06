from frontend.ui_manager import UIManager
from utils.logger import get_logger
logger = get_logger("main_logger", "app.log")

if __name__ == "__main__":
    UIManager().display_dashboard()    
    logger.info("App started")