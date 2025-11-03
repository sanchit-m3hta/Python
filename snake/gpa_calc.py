import pandas as pd
import os
import sys

grades_file = "/Users/shallow/Desktop/Languages/snake/grades.csv"
grading_scale_file = "/Users/shallow/Desktop/Languages/snake/grading_scale.csv"

#letter-grade to gpa dictionary
grading_scale = pd.read_csv(grading_scale_file).set_index('Grade')['GPA'].to_dict()


def read_file():
    try:
        df = pd.read_csv(grades_file)
        print(f"Read '{os.path.split(grades_file)[1]}' successfully")
        return df
    except Exception as e:
        print(f"Failed to read '{os.path.split(grades_file)[1]}': {e}")
        sys.exit(1)

def convert_letter_grade_to_gpa(letter_grades):
    grades = [grading_scale[entry] for entry in letter_grades]
    return grades

def calculate_cgpa(grade_points_earned, units):
    total_grade_points = 0
    for points in grade_points_earned:
        total_grade_points += points
    
    total_units = 0
    for unit in units:
        total_units += unit

    return total_grade_points/total_units

def main():
    df = read_file()
    #print(f"Read {len(df)} Grades: \n", df)

    letter_grades = df['Grade'].tolist()
    letter_grades = [grade.upper() for grade in letter_grades]

    units = df['Units'].tolist()

    grades = convert_letter_grade_to_gpa(letter_grades)

    grade_points_earned = []
    for i, grade in enumerate(grades):
        grade_points_earned.append(grade*units[i])
    
    gpa = 0
    gpa = calculate_cgpa(grade_points_earned, units)
    print(f"Your CGPA is: {gpa:.2f}")


if __name__ == "__main__":
    main()