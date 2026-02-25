text = input("Enter a sentence: ")

words = text.split()
title_case = ""

for word in words:
    title_case += word[0].upper() + word[1:].lower() + " "

print("Title case string:", title_case.strip())