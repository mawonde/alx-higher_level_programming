#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except:
            break
        else:
            num += 1

    print()
    return (num)
