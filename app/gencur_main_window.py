### GUI imports
from guizero import *
from gencur_main import *
import pygame

### GUI functions
def cml():
    try:
        weight = float(txtbox_weight.value)
        af = float(combo_af.value)  # Get the value from the combo box
        cml = cml1(weight, af)
        text_welcome.value = f"Tvoje CML je {cml} kcal"
        image_widget.image = "T:\G6_2025\Genčur\G6\Student-Python-App-1---Starting-Files-main\Student-Python-App-1---Starting-Files-main\App\Resources\images\calculating_cml.png"  # Nastavení obrázku na výchozí "CML"
    except ValueError:
        text_welcome.value = "Zadej platná čísla"

# Function to handle game selection and display the result
def handle_game_selection():
    # Check which radio button is selected
    if rb_fortnite.value:
        selected_game = "Fortnite"
    elif rb_lol.value:
        selected_game = "League of Legends"
    result = handle_game_choice(selected_game)  # Send the selection to the backend
    text_game_result.value = result  # Display the result in the frontend

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("T:\G6_2025\Genčur\G6\Student-Python-App-1---Starting-Files-main\Student-Python-App-1---Starting-Files-main\App\Resources\gencur_audio.mp3")  # Cesta k vašemu zvuku
    pygame.mixer.music.play()
    image_widget.image = "T:\G6_2025\Genčur\G6\Student-Python-App-1---Starting-Files-main\Student-Python-App-1---Starting-Files-main\App\Resources\images\gencur_images.png"  # Přepnutí obrázku na "roonie"

def stop_sound():
    pygame.mixer.music.stop()
    image_widget.image = "T:\G6_2025\Genčur\G6\Student-Python-App-1---Starting-Files-main\Student-Python-App-1---Starting-Files-main\App\Resources\images\calculating_cml.png"  # Vrátí obrázek na výchozí stav

### GUI App
app = App(title="My App", width=680, height=1000, layout="grid")

# Welcome text
text_welcome = Text(app, text="Hi, user!", size=16, grid=[0, 0], align="center")

# Input activity factor (via Combo Box)
text_af = Text(app, text="Please select your activity factor:", grid=[0, 1], align="center")
combo_af = Combo(
    app,
    options=["1.2", "1.375", "1.55", "1.725", "1.9"],  # Common activity factor values
    selected="1.2",
    grid=[0, 2],
    align="center",
)

# Input weight
text_weight = Text(app, text="Please enter your weight in kilograms (kg):", grid=[0, 3], align="center")
txtbox_weight = TextBox(app, grid=[0, 4], align="center")

# Spacer for button
button_spacer = Box(app, height=10, width="fill", grid=[0, 5])  # Adds a small gap before the button

# Button to calculate CML
button = PushButton(
    app,
    command=cml,
    text="Vypočítej",
    grid=[0, 6],
    align="center",
    width=10,  # Smaller width
)

# Spacer for positioning the image lower
spacer = Box(app, height=50, width="fill", grid=[0, 7])  # Adds space below the button

# Display an image (centered)
image_widget = Picture(
    app,
    image="T:\G6_2025\Genčur\G6\Student-Python-App-1---Starting-Files-main\Student-Python-App-1---Starting-Files-main\App\Resources\images\calculating_cml.png",
    width=680,  # Adjusted image size
    height=480,  # Adjusted image size
    grid=[0, 8],
    align="center",
)

# Game selection section (below the image)
text_game_choice = Text(app, text="Which game do you prefer?", grid=[0, 9], align="center")

# Radio buttons to choose a game
rb_fortnite = CheckBox(app, text="Fortnite", grid=[0, 10], align="center")
rb_lol = CheckBox(app, text="League of Legends", grid=[0, 11], align="center")

# Button to submit game choice
game_button = PushButton(
    app,
    command=handle_game_selection,
    text="Submit",
    grid=[0, 12],
    align="center",
)

# Text to display the result from the backend
text_game_result = Text(app, text="", grid=[0, 13], align="center")

# Spacer for sound buttons
sound_spacer = Box(app, height=20, width="fill", grid=[0, 14])

# Buttons to control sound
text_sound_control = Text(app, text="Sound Control:", grid=[0, 15], align="center")
play_button = PushButton(app, command=play_sound, text="Play Sound", grid=[0, 16], align="center")
stop_button = PushButton(app, command=stop_sound, text="Stop Sound", grid=[0, 17], align="center")

app.display()