# gencur_gui.py

from guizero import App, Text, TextBox, PushButton, Combo, CheckBox, Box, Picture
from gencur_main import display_cml, activity_factor_changed  # Importujeme funkce z main.py
from gencur_config import APP_TITLE, APP_WIDTH, APP_HEIGHT

# App configuration
app = App(title=APP_TITLE, width=APP_WIDTH, height=APP_HEIGHT)

# Central container
central_box = Box(app, align="top", width="fill", height="fill")

# Welcome text
text_welcome = Text(central_box, text="Hi, user!", align="top")

# Input: Activity Factor
text_af = Text(central_box, text="Select your activity factor:", align="top")
combo_af = Combo(central_box, options=["1.2", "1.5", "1.7", "2.0"], align="top", command=lambda: activity_factor_changed(text_cml))

# Input: Weight
text_weight = Text(central_box, text="Enter your weight in kilograms (kg):", align="top")
txtbox_weight = TextBox(central_box, align="top")

# Input: Extra Factor CheckBox
checkbox_extra_factor = CheckBox(central_box, text="Include extra factor (10%)", align="top")

# Output: CML
text_cml = Text(central_box, text="", align="top")

# Button to calculate CML
btn_calculate = PushButton(central_box, text="Calculate CML", command=lambda: display_cml(txtbox_weight, combo_af, checkbox_extra_factor, text_cml), align="top")

# Display an image
image_widget = Picture(central_box, image="resources/images/calculating_cml.png", width=680, height=480, align="top")

# Run the app
app.display()
