text = input("Enter a string: ")

# Generate substrings using nested loops
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])