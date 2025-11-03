# Grade to GPA mapping
grade_to_gpa = {
    "A+": 9,
    "A": 8,
    "A-": 7,
    "B+": 6,
    "B": 5,
    "B-": 4,
    "C+": 3,
    "C": 2,
    "D": 1,
    "F": 0
}

def read_grades_from_file(filename):
    total_units = 0.0
    total_weighted_gpa = 0.0

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Skip header
            for line in lines[1:]:
                parts = line.strip().split()
                if len(parts) < 3:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue

                course = parts[0]
                grade = parts[1].upper()
                try:
                    units = float(parts[2])
                except ValueError:
                    print(f"Invalid unit value for course {course}. Skipping.")
                    continue

                if grade not in grade_to_gpa:
                    print(f"Invalid grade '{grade}' for course {course}. Skipping.")
                    continue

                gpa = grade_to_gpa[grade]
                total_units += units
                total_weighted_gpa += gpa * units

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    if total_units == 0:
        print("No valid data to calculate GPA.")
    else:
        cgpa = total_weighted_gpa / total_units
        print(f"\nYour calculated GPA is: {cgpa:.2f}")

# Main execution
filename = input("Enter the filename containing the grades (e.g., grades.txt): ")
read_grades_from_file(filename)
