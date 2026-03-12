paper1 = int(input("Enter marks for Paper 1: "))
paper2 = int(input("Enter marks for Paper 2: "))
paper3 = int(input("Enter marks for Paper 3: "))

total_marks = paper1 + paper2 + paper3
percentage = (total_marks / 300) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 60:
    print("Eligible for placement")
else:
    print("Not eligible for placement")