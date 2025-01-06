# Import GUI library and backend functions
from guizero import App, Box, Text, TextBox, PushButton, Picture
from gencur_main import calculate_cml
from gencur_config import APP_TITLE, APP_WIDTH, APP_HEIGHT

# GUI functions
def display_cml():
    """
    Fetch inputs from GUI, calculate CML, and display the result.
    """
    try:
        weight = float(txtbox_weight.value)
        activity_factor = float(txtbox_af.value)
        cml = calculate_cml(weight, activity_factor)
        text_cml.value = f"Your Calorie Maintenance Level (CML) is {cml:.2f} kcal/day."
    except ValueError:
        text_cml.value = "Please enter valid numbers for weight and activity factor."

# App configuration
app = App(title=APP_TITLE, width=APP_WIDTH, height=APP_HEIGHT)

# Main window
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text="Hi, user!")

# Input: Activity Factor
text_af = Text(window1, text="Enter your activity factor:")
txtbox_af = TextBox(window1)

# Input: Weight
text_weight = Text(window1, text="Enter your weight in kilograms (kg):")
txtbox_weight = TextBox(window1)

# Output: CML
text_cml = Text(window1, text="")

# Button to calculate CML
btn_calculate = PushButton(window1, text="Calculate CML", command=display_cml)

# Display an image
image_widget = Picture(window1, image="resources/images/calculating_cml.png", width=680, height=480, align="bottom")

# Run the app
app.display()
