dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Manual merge
for key in dict2:
    dict1[key] = dict2[key]

print("Merged dictionary:", dict1)