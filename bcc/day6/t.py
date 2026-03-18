name = "dev *is*a*good*programmer"
new_name = ''
val=''
for i in name:
    if i!='*':
        new_name+=i
    else:
        val+=i
print(new_name)
print(str(val+new_name))