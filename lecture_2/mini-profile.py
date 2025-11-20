def generate_profile(age):
    """Defines a Function for the Profile & Calculation"""
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:  # age 20 or older
        return "Adult"
    
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

current_year = 2025
current_age = current_year - birth_year
    
life_stage = generate_profile(current_age)


hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)

user_profile = {"name":user_name, "age":current_age, "stage":life_stage, "hobbies":hobbies}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if not user_profile['hobbies']:
        print("You didn't mention any hobbies.")
else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")
    
print("---")
        