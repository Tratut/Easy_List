def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_same_parts_list(mass):
    for i in range(1, len_list(mass)):
        if mass[i] == mass[i - 1]:
            return True
    return False

# print(ft_same_parts_list([1, 4, 2, 3]))
