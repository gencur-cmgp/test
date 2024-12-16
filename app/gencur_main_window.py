### GUI imports
from guizero import *
from gencur_main import *

### GUI functions
def my_first_gui_function():
    # Získání hodnot z textových polí
    try:
        weight = float(txtbox_weight.value)  # Hmotnost
        activity_factor = float(txtbox_af.value)  # Aktivitní faktor
        
        # Výpočet BMR
        bmr = weight * 24.2
        
        # Výpočet CML
        cml = bmr * activity_factor
        
        # Aktualizace textu uvítání s výsledkem CML
        text_cml.value = f"Hi, user! Your Calorie Maintenance Level (CML) is {cml:.2f} kcal/day."
        
    except ValueError:
        # Pokud jsou hodnoty neplatné (např. uživatel nezadá číslo)
        text_cml.value = "Please enter valid numbers for weight and activity factor."

        
### GUI App
app = App(title="My App", width=775, height=650)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Please enter your activity factor for today:"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

welcome_button = PushButton(window1,command=my_first_gui_function)

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

app.display()

