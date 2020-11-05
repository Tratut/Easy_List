def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_rev_par_list(mass):
    long = len_list(mass)
    for i in range(1, long, 2):
        x = mass[i - 1]
        u = mass[i]
        mass[i - 1] = u
        mass[i] = x
    return mass

# print(ft_rev_par_list([1, 2, 3, 4, 5, 6, 7]))
