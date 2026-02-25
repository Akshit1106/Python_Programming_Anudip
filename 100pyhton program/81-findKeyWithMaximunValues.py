d = {"a": 10, "b": 25, "c": 15}

max_key = max(d, key=d.get)

print("Key with maximum value:", max_key)