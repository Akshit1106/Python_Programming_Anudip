text = input("Enter a string: ")

compressed = ""
count = 1

# Loop through string
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        compressed += text[i-1] + str(count)
        count = 1

# Add last character
compressed += text[-1] + str(count)

print("Compressed string:", compressed)