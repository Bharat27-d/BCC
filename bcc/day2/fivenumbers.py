a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
e = int(input("Enter 5th number: "))

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if d > max_val:
    max_val = d
if e > max_val:
    max_val = e

print("Maximum value is:", max_val)