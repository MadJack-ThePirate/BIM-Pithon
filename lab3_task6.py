list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

last_max_indx = None
indicator = 1

for indx, num in enumerate(list_numbers):
    for num_1 in list_numbers:
        if num < num_1:
            indicator = 0
    if indicator:
        last_max_indx = indx
    indicator = 1

list_numbers[-1], list_numbers[last_max_indx] = list_numbers[last_max_indx], list_numbers[-1]

print(list_numbers)
#  отступ
