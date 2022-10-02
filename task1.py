# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import math



d = str(input("введите точность числа пи: "))

d = len(str(d).split('.')[1])
pi = math.pi
print(pi)
st_pi = str(round(pi, d+1))
l = len(st_pi) - 1
print(st_pi.replace(st_pi[l], ''))
