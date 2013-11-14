import re
en = "Very Strong Fat Cat"
en = re.split(" ",en)
for word in en:
    print(word[0])