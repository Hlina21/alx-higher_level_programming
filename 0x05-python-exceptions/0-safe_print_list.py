#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    ret = 0
    for i in range(y):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
