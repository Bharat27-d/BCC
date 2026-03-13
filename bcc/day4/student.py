n=int(input("Enter the number of students: "))
d={}
for i in range(n):
    name=input("Enter name of student: ")
    marks=int(input("Enter marks of student: "))
    d[name]=marks
while True:
    name=input("Enter your name: ")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student not found")
    else:
        print("Marks of",name,"are",marks)
    option=input("Do you want to find marks of another student? (y/n): ")
    if option.lower() == "n":
        break
print("Thank you")