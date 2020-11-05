def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_rev_par_list(mass):
    for i in range(len_list(mass) // 2):
        x = mass[0 + i]
        u = mass[len_list(mass)-i]
        mass[0 + i] = u
        mass[len_list(mass) - i] = x
    return mass


print(ft_rev_par_list([1, 2, 3, 4, 5, 6]))
