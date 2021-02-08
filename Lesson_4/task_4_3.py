# ----- task 3 --------
def my_gen_1(start, end):
    i = start
    while i <= end:
        yield i
        i += 1


def my_gen_2(start, end):
    i = start
    while i <= end:
        if i % 20 == 0 or i % 21 == 0:
            yield i
            i += 1
        else:
            i += 1


# --- var 1 -------
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# --- var 2 -------
print([el for el in my_gen_1(20, 241) if el % 20 == 0 or el % 21 == 0])

# --- var 3 -------
print([el for el in my_gen_2(20, 241)])
