list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]
for i, current_number in enumerate(list_numbers):
    if current_number >= max_number:
        max_number = current_number
        index = i

list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]

print(list_numbers)
