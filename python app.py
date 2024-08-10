healthcare_app/
├── app.py
└── medications.py
medications_db = {
    'hypertension': ['Lisinopril', 'Amlodipine', 'Hydrochlorothiazide'],
    'diabetes': ['Metformin', 'Insulin', 'Glipizide'],
    'obesity': ['Orlistat', 'Phentermine', 'Liraglutide'],
    'cholesterol': ['Atorvastatin', 'Rosuvastatin', 'Simvastatin'],
    'heart disease': ['Aspirin', 'Clopidogrel', 'Nitroglycerin'],
    'arthritis': ['Ibuprofen', 'Naproxen', 'Celecoxib'],
    'asthma': ['Albuterol', 'Fluticasone', 'Montelukast']
}

def get_medications(diseases):
    medications = []
    for disease in diseases:
        if disease.lower() in medications_db:
            medications.extend(medications_db[disease.lower()])
    return medications
from medications import get_medications

def get_health_info():
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in cm): "))
    weight = float(input("Enter your weight (in kg): "))
    fat_percentage = float(input("Enter your body fat percentage: "))

    diseases = input("Enter any known diseases (separated by commas): ").split(',')
    diseases = [disease.strip() for disease in diseases]

    return {
        'age': age,
        'height': height,
        'weight': weight,
        'fat_percentage': fat_percentage,
        'diseases': diseases
    }

def provide_medications(user_info):
    medications = get_medications(user_info['diseases'])
    if medications:
        print("\nBased on your conditions, the following medications are recommended:")
        for medication in medications:
            print(f"- {medication}")
    else:
        print("\nNo specific medications are recommended based on the provided conditions.")

def main():
    print("Welcome to the Healthcare App")
    user_info = get_health_info()

    print("\nUser Information:")
    print(f"Age: {user_info['age']} years")
    print(f"Height: {user_info['height']} cm")
    print(f"Weight: {user_info['weight']} kg")
    print(f"Body Fat Percentage: {user_info['fat_percentage']}%")
    print(f"Diseases: {', '.join(user_info['diseases']) if user_info['diseases'] else 'None'}")

    provide_medications(user_info)

if __name__ == "__main__":
    main()
