# Ввод количество строк в массиве
n = int(input("Введите количество строк в массиве: "))

# Создание пустого массива array
array = []

# Ввод строк с клавиатуры и добавление их в массив array
for i in range(n):
    string = input(f"Введите строку {i+1}: ")
    array.append(string)

# Создание пустого массива filtered_array
filtered_array = []

# Фильтрация массива и добавление отфильтрованных строк в filtered_array
for string in array:
    if len(string) <= 3:
        filtered_array.append(string)

# Вывод результата
print("Отфильтрованный массив:")
for string in filtered_array:
    print(string)