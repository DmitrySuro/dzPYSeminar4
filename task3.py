# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

succession_digits = [23,1,4,23,2421,321,5867,34,97]
uniq_digits = []
for i in succession_digits:
    elem = i
    for j in succession_digits:
        if elem == j:
            uniq_digits.append(elem)
            break

print(uniq_digits)
        



    