# Importing all app imports
from gencur_config import *

# Main Window Functions
def cml1(weight, af):
           bmr = weight * 24.2
           cml = bmr * af
           return cml    
    
def handle_game_choice(game):
    return f"User prefers: {game}"                
        


# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries

