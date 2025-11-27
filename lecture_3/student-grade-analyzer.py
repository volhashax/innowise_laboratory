def main():
    """
    Main function that runs the Student Grade Management System.
    
    This program provides a menu-driven interface to manage student data including:
    - Adding new students
    - Adding grades for students
    - Generating reports
    - Finding top performers
    
    The program runs in an infinite loop until the user chooses to exit.
    """
    
    students = []  # List of student dictionaries
    
    while True:
        # Display menu
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit ptogram")
        
        # Get user choice with error handling
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                add_new_student(students)
            elif choice == '2':
                add_grades_for_student(students)
            elif choice == '3':
                show_report(students)
            elif choice == '4':
                find_top_performer(students)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def add_new_student(students):
    """
    Main function that runs the Student Grade Management System.
    
    This program provides a menu-driven interface to manage student data including:
    - Adding new students
    - Adding grades for students
    - Generating reports
    - Finding top performers
    
    The program runs in an infinite loop until the user chooses to exit.
    """
    # Ask for the new student's name
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return
    
    # Check if student already exists
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Error: A student named '{name}' already exists.")
            return
    
    # Create new student dictionary
    new_student = {
        "name": name,
        "grades": []
    }
    
    # Add to students list
    students.append(new_student)

def add_grades_for_student(students):
    """
    Add grades for an existing student.
    
    Args:
        students (list): List of student dictionaries to search and modify
        
    Process:
        - Validates that students exist in system
        - Finds student by name (case-insensitive)
        - Continuously accepts grade inputs (0-100)
        - Validates each grade before adding to student's record
        - Allows user to stop input with 'done' command
    """
    
    # Check if there are any students
    if not students:
        print("No students available. Please add a student first.")
        return
    
    # Prompt for student name
    name = input("Enter student name: ").strip()
    
    # Find the student
    student_found = None
    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break
    
    if not student_found:
        print(f"Error: Student '{name}' not found.")
        return
    
    # Add grades for the found student
    
    while True:
        grade_input = input("Enter a grade (or 'done' to finish):").strip().lower()
        
        # Check if user wants to stop
        if grade_input == 'done':
            break
        
        # Validate and add grade
        try:
            grade = int(grade_input)
            
            if 0 <= grade <= 100:
                student_found["grades"].append(grade)
            else:
                print("Error: Grade must be between 0 and 100.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_report(students):
    """
    Generate and display a comprehensive report of all students.
    
    Args:
        students (list): List of student dictionaries to analyze
        
    Process:
        - Checks if students and grades exist
        - Calculates individual student averages
        - Handles students with no grades (N/A)
        - Displays overall statistics (max, min, overall average)
    """
    print("--- Student Report ---")
    
    # Check if there are any students
    if not students:
        print("No students available.")
        return
    
    # Check if any student has grades
    has_grades = any(student["grades"] for student in students)
    if not has_grades:
        print("No grades available for any student.")
        return
    
    averages = []
    
    # Iterate through students and calculate averages
    for student in students:
        name = student["name"]
        grades = student["grades"]
        
        try:
            if grades:  # If student has grades
                average = sum(grades) / len(grades)
                averages.append(average)
                print(f"{name}'s average grade is {average:.1f}.")
            else:  # Student has no grades
                print(f"{name}'s average grade is N/A.")
                
        except ZeroDivisionError:
            print(f"{name}'s average grade is N/A.")
    
    # Print overall summary
    if averages:  # Only print summary if we have calculated averages
        print("----------------------")
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages) / len(averages):.1f}")

# Placeholder function for remaining menu option
def find_top_performer(students):
    """
    Find and display the student with the highest average grade.
    
    Args:
        students (list): List of student dictionaries to analyze
        
    Process:
        - Filters out students with no grades
        - Uses lambda function with max() to find top performer
        - Handles cases with no students or no grades
        - Displays top student name and average grade
    """
    
    # Check if there are any students
    if not students:
        print("No students available.")
        return
    
    # Filter out students with no grades
    students_with_grades = [student for student in students if student["grades"]]
    
    # Check if any student has grades
    if not students_with_grades:
        print("No students with grades available.")
        return
    
    # Find top performer using max() with lambda function
    try:
        top_student = max(students_with_grades, 
                         key=lambda student: sum(student["grades"]) / len(student["grades"]))
        
        # Calculate the average grade for the top student
        top_average = sum(top_student["grades"]) / len(top_student["grades"])
        
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")
        
    except (ValueError, ZeroDivisionError) as e:
        print("Error: Unable to determine top performer due to invalid data.")

# Run the program
if __name__ == "__main__":
    main()