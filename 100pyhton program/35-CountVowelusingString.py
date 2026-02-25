text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels are:", count)