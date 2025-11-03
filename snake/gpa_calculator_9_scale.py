valid_grades = {'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F'}

grade_dictionary_900_scale = {'A+': '9.0',
                     'A': '8.0',
                     'A-': '7.0',
                     'B+': '6.0',
                     'B':'5.0',
                     'B-': '4.0',
                     'C+': '3.0',
                     'C': '2.0',
                     'D': '1.0',
                     'F': '0.0'}

grad_dictionary_433_scale  = {'A+': '4.33',
                            'A': '4.00',
                            'A-': '3.67',
                            'B+': '3.33',
                            'B': '3.00',
                            'B': '2.67',
                            'C+': '2.33',
                            'C': '2.00',
                            'D': '1.67',
                            'F': '0.00'}

def get_letter_grades():
    grades = []
    while True: 
        grade = input("enter grades in 9.0 scale (e or E to stop): ").strip().upper()
        if grade.lower() == 'e':
            print("finished entering grades")   
            break
        if grade in grade_dictionary_900_scale:
            grades.append(grade)
        else:
            print("not a valid grade")
    return grades

def get_course_units(grades):
    course_units = []
    for grade in grades:
        units = input("enter course units for grade: ")
        course_units.append(units)
    return course_units

def clear_screen():
    print("")
    print("")

if __name__ == "__main__":
    clear_screen()
    grades = get_letter_grades()
    print(f"Entered grades: {grades}")
    course_units = get_course_units(grades)
    print(f"Entered course units: {course_units}")




