# Take input string
text = input("Enter a string: ")

# Dictionary to store frequency
freq = {}

# Count frequency of each character
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Find first character with frequency 1
for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found.")