def get_unique_list_numbers():
    from random import randint
    numbers = []
    counter = 15
    while counter != 0:
        i = randint(-10, 10)
        if i in numbers:
            continue
        else:
            numbers.append(i)
            counter -= 1
    return(numbers)
print(get_unique_list_numbers())



