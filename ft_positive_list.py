def len_list(mass):
    i = 0
    for g in mass:
        i += 1
    return i


def ft_positive_list(mass):
    count = 0
    for i in range(len_list(mass)):
        if mass[i] >= 0:
            count += 1
    return count

# print(ft_positive_list([1, 2, 3, 4, 5,-6]))
