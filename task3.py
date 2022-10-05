# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


succession_digits = [1, 2, 3546, 2, 5, 8, 4, 4, 4, 1, 8, 9, 99, 9]

my_list = []

for elem in succession_digits:
    if succession_digits.count(elem) == 1:
        my_list.append(elem)

print(my_list)
