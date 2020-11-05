def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_sl_list(mass):
    count = 0
    for i in range(1, len_list(mass)):
        if mass[i] > mass[i - 1]:
            count += 1
    return count

# print(ft_sl_list([1, 2, 2, 3, 4, 4]))
