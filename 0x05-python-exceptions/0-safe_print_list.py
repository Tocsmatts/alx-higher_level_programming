#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numcount = 0

    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
        except Exception:
            break
        else:
            numcount += 1

    print()
    return(numcount)
