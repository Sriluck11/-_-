def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

get_user_input()
