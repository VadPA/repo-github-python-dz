def my_func(a, b, c):
    if a < b and a < c:
        res = b + c
    elif b < a and b < c:
        res = a + c
    else:
        res = a + b
    return res

print(f'Результат:{my_func(9, 120, 120)}')