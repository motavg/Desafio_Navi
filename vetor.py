from math import factorial
from math import log as ln
x = list(range(10))
print(x)

for i in x:
    if i % 2 == 0:
        x[i] = (3**i) + 7 * (factorial(i))
    else:
        x[i] = round((2**i) + 4 * (ln(i)), 2)

print(x)
max_value = max(x)

print(f"O maior valor é {max(x, key=int)}, na posição {x.index(max_value)}")
