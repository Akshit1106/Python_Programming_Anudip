numbers = list(map(int, input("Enter numbers: ").split()))

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list is:", reversed_list)