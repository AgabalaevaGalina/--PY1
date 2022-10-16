list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0

for i in range(len(list_numbers)):  # перебераем все индексы
    max_current = list_numbers[max_index]
    current_number = list_numbers[i]
    if current_number > max_current:  # если текущий значение больше того, которое встречали ранее
        max_index = i
tuple_vars = list_numbers
list_numbers[19], list_numbers[max_index] = list_numbers[max_index], list_numbers[19]
print(tuple_vars)