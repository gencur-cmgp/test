# gencur_main.py

def calculate_cml_with_factor(weight, activity_factor, include_extra_factor):
    """
    Calculate the Calorie Maintenance Level (CML) with an optional extra factor.
    :param weight: Weight in kilograms
    :param activity_factor: Activity factor
    :param include_extra_factor: Boolean to include an extra 10% factor
    :return: CML in kcal/day
    """
    try:
        bmr = weight * 24.2  # Basic Metabolic Rate
        cml = bmr * activity_factor
        if include_extra_factor:
            cml *= 1.10  # Adding an extra 10%
        return cml
    except (ValueError, TypeError):
        raise ValueError("Invalid inputs for weight or activity factor.")

def display_cml(txtbox_weight, combo_af, checkbox_extra_factor, text_cml):
    """
    Fetch inputs from GUI, calculate CML, and display the result in the GUI.
    """
    try:
        weight = float(txtbox_weight.value)
        activity_factor = float(combo_af.value)
        include_extra_factor = checkbox_extra_factor.value
        cml = calculate_cml_with_factor(weight, activity_factor, include_extra_factor)
        text_cml.value = f"Your Calorie Maintenance Level (CML) is {cml:.2f} kcal/day."
    except ValueError:
        text_cml.value = "Please enter valid numbers for weight and activity factor."

def activity_factor_changed(text_cml):
    """
    Function to handle the change in activity factor.
    """
    text_cml.value = "Activity factor changed, you can recalculate your CML."