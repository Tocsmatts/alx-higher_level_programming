#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) > 1:
        length = len(sys.argv)
        sum = 0
        for i in range(1, length):
            sum += int(sys.argv[i])
        print(sum)
