def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_even_index_list(mass):
    mass_cop = []
    for i in range(0, len_list(mass), 2):
        mass_cop.append(mass[i])
    return mass_cop

# print(ft_even_index_list([1, 2, 3, 4, 5, 6]))
