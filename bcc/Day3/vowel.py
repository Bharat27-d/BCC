name = "prashant"

newname = ''

vowels = "aeiou"
v_c= 0
c_c = 0

for ch in name:
    if ch in vowels:
        v_c += 1
    else:
        c_c += 1

print("Vowels:", v_c)

