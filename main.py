def get_grade(subject):
    while True:
        user_input = input(f"Enter grade for {subject}: ")
        try:
            grade = float(user_input)
            return grade
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

def get_student_info():
    name = input("Enter student's name: ")
    english = get_grade("English")
    math = get_grade("Math")

    student = {
        "Name": name,
        "English": english,
        "Math": math
    }
    return student

def print_student_info(students):
    for student in students:
        name = student["Name"]
        english = student["English"]
        math = student["Math"]

        grades = [english, math]
        best_grade = max(grades)
        avg_grade = sum(grades) / len(grades)

        print(f"{name}: Best grade = {best_grade}, Average grade = {avg_grade:.2f}")

def calculate_average_grades(students):
    sum_english = 0
    sum_math = 0
    n = len(students)

    for student in students:
        sum_english += student["English"]
        sum_math += student["Math"]

    avg_english = sum_english / n
    avg_math = sum_math / n

    average_grades_per_subject = {
        "English": avg_english,
        "Math": avg_math
    }

    total_sum = sum_english + sum_math
    total_count = 2 * n
    overall_average = total_sum / total_count

    return average_grades_per_subject, overall_average

def calculate_failing_grades(students):
    failing_per_student = {}
    total_failing = 0

    for student in students:
        name = student["Name"]
        english = student["English"]
        math = student["Math"]

        count = 0
        if english <= 55:
            count += 1
        if math <= 55:
            count += 1

        failing_per_student[name] = count
        total_failing += count

    return failing_per_student, total_failing

def main():
    num_students = int(input("How many students? "))
    students = []

    for _ in range(num_students):
        student = get_student_info()
        students.append(student)

    print_student_info(students)

    average_grades_per_subject, overall_average_grade = calculate_average_grades(students)

    print("\nAverage grades per subject:")
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")

    failing_per_student, total_failing = calculate_failing_grades(students)

    print("\nFailing grades per student:")
    for name, count in failing_per_student.items():
        print(f"{name}: {count} failing grade(s)")

    print(f"\nTotal number of failing grades across all students: {total_failing}")

if __name__ == "__main__":
    main()
