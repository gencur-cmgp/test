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