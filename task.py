def filter_strings(array):
    result = []
    for string in array:
        if len(string) <= 3:
            result.append(string)
    return result

# Ввод массива строк с клавиатуры
n = int(input("Введите количество строк в массиве: "))
array = []
for i in range(n):
    string = input(f"Введите строку {i+1}: ")
    array.append(string)

# Фильтрация массива
filtered_array = filter_strings(array)

# Вывод результата
print("Отфильтрованный массив:")
for string in filtered_array:
    print(string)