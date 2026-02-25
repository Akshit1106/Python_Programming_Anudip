d = {"a": 3, "b": 1, "c": 2}

# Sort by values
sorted_items = sorted(d.items(), key=lambda x: x[1])

for key, value in sorted_items:
    print(key, ":", value)