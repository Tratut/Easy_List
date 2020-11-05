def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_even_parts_list(mass):
    mass_cop = []
    for i in range(len_list(mass)):
        if mass[i] % 2 == 0:
            mass_cop.append(mass[i])
    return mass_cop

# print(ft_even_parts_list([1, 2, 3, 4, 5, 6]))
