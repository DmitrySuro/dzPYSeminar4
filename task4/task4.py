# Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (значения от 0 до 100) многочлена и
#   записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = random.randint(0,101)
poly = '2*x**k + 4*x + 5 = 0'
poly.replace('k', str(k))

data = open('File.txt', 'a')
data.writelines(poly.replace('k', str(k)))
data.close()