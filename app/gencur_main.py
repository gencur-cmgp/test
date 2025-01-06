# Import statements
import datetime as dt

# Backend function to calculate Calorie Maintenance Level (CML)
def calculate_cml(weight, activity_factor):
    """
    Calculate the Calorie Maintenance Level (CML).
    :param weight: Weight in kilograms
    :param activity_factor: Activity factor
    :return: CML in kcal/day
    """
    try:
        bmr = weight * 24.2  # Basic Metabolic Rate
        cml = bmr * activity_factor  # Calorie Maintenance Level
        return cml
    except (ValueError, TypeError):
        raise ValueError("Invalid inputs for weight or activity factor.")

# Example usage
if __name__ == "__main__":
    # Test the function directly
    weight = 70  # kg
    activity_factor = 1.2
    print(f"CML: {calculate_cml(weight, activity_factor):.2f} kcal/day")
