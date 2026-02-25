keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Created dictionary:", d)