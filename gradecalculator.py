def calculate_grade(marks):
    if marks >= 90:
        grade = "A"
        message = "Excellent work! You’re truly shining! "
    elif marks >= 80:
        grade = "B"
        message = "Great job! Keep up the strong effort! "
    elif marks >= 70:
        grade = "C"
        message = "Good! A little more push and you’ll reach higher! "
    elif marks >= 60:
        grade = "D"
        message = "You're improving! Keep practicing and you’ll get there! "
    else:
        grade = "F"
        message = "Don't worry—every setback is a setup for a comeback! Try again! "
    
    return grade, message


marks = float(input("Enter the student's marks (0–100): "))
grade, message = calculate_grade(marks)

print(f"Grade: {grade}")
print("Message:", message)
