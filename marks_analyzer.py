# Student Marks Analyzer
# A simple Python program to calculate average, highest, lowest marks and grade range.

def calculate_statistics(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    return highest, lowest, average


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "D"


def main():
    print("\n📘 Student Marks Analyzer\n")

    n = int(input("Enter number of subjects: "))

    marks = []
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    highest, lowest, average = calculate_statistics(marks)
    grade = assign_grade(average)

    print("\n--- Results ---")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")
    print(f"Overall Grade: {grade}")


if __name__ == "__main__":
    main()
