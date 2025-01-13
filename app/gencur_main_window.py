from guizero import App, Text, TextBox, PushButton, Picture, Combo, CheckBox
from gencur_main import calculate_cml_with_factor
from gencur_config import APP_TITLE, APP_WIDTH, APP_HEIGHT

# GUI functions
def display_cml():
    """
    Fetch inputs from GUI, calculate CML, and display the result.
    """
    try:
        weight = float(txtbox_weight.value)
        activity_factor = float(combo_af.value)
        include_extra_factor = checkbox_extra_factor.value
        cml = calculate_cml_with_factor(weight, activity_factor, include_extra_factor)
        text_cml.value = f"Your Calorie Maintenance Level (CML) is {cml:.2f} kcal/day."
    except ValueError:
        text_cml.value = "Please enter valid numbers for weight and activity factor."

# App configuration
app = App(title=APP_TITLE, width=APP_WIDTH, height=APP_HEIGHT, layout="grid")

# Welcome text
text_welcome = Text(app, text="Hi, user!", grid=[0, 0, 2, 1])

# Input: Activity Factor
text_af = Text(app, text="Select your activity factor:", grid=[0, 1])
combo_af = Combo(app, options=["1.2", "1.5", "1.7", "2.0"], grid=[1, 1])

# Input: Weight
text_weight = Text(app, text="Enter your weight in kilograms (kg):", grid=[0, 2])
txtbox_weight = TextBox(app, grid=[1, 2])

# Input: Extra Factor CheckBox
checkbox_extra_factor = CheckBox(app, text="Include extra factor (10%)", grid=[0, 3, 2, 1])

# Output: CML
text_cml = Text(app, text="", grid=[0, 4, 2, 1])

# Button to calculate CML
btn_calculate = PushButton(app, text="Calculate CML", command=display_cml, grid=[0, 5, 2, 1])

# Display an image
image_widget = Picture(app, image="resources/images/calculating_cml.png", grid=[0, 6, 2, 1], width=680, height=480)

# Run the app
app.display()