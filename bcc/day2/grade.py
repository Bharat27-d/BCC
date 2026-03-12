percentage = float(input("Enter percentage: "))

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
else:
    grade = 'Fail'

print(f"Grade: {grade}")