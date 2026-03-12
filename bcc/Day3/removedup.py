name = "prashant"

newname = ''

for i in name:
    if i not in newname:
        newname += i

print("Name without duplicates:", newname)