text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print("Updated string:", result)