def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_rshift_list(mass):
    mass.insert(0, mass[-1])
    mass.pop()
    return mass

# print(ft_rshift_list([1, 2, 3, 4, 5, 6]))
