import os
import datetime as dt
from datetime import date, datetime, timedelta

# Working directory configuration
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Constants
APP_TITLE = "My Future App"
APP_WIDTH = 775
APP_HEIGHT = 650

print(f"Current working directory is: {os.getcwd()}")