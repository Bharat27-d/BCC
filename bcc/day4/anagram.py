str1="listen"
str2="silent"

for i in str1:
    if i in str2:
        str2=str2.replace(i,"",1)
    else:
        print("Not anagram")
        break
    