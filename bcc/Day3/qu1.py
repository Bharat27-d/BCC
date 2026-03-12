ch = input("Enter a character: ")

if ch.isupper():
    print(f"'{ch}' is uppercase")
elif ch.islower():
    print(f"'{ch}' is lowercase")
elif ch.isdigit():
    print(f"'{ch}' is a digit")
else:
    print(f"'{ch}' is a special symbol")