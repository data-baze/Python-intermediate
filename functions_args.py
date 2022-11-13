def add_numbers(name, *args):
    total = 0
    for num in args:
        total = total + num
    return total

total = add_numbers(1, 2, 4, 6, 8,)
print(total)