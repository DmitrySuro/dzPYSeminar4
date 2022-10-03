# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from decimal import Decimal
p = input('Insert your float number: ')
accuracy = input('Insert accuracy: ')
p = Decimal(p)
p = p.quantize(Decimal(accuracy))
print(p)