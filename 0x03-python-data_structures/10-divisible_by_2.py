#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x_by_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            x_by_2.append(True)
        else:
            x_by_2.append(False)

    return (x_by_2)
