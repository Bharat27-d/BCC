ch = ord(input("Enter a character: "))

if ch>=65 and ch<=91:
    print(f"'{chr(ch)}' is uppercase")
elif ch>=97 and ch<=122:
    print(f"'{chr(ch)}' is lowercase")
elif ch>=48 and ch<=57:
    print(f"'{chr(ch)}' is a digit")
else:
    print(f"'{chr(ch)}' is a special symbol")
    