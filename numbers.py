#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 3, 2022
# This program uses a while loop


def main():
    # this function uses a while loop
    loop_counter = 0

    # input
    positive_integer_as_string = input("Enter any positive integer: ")
    print("")

    # process & output
    while loop_counter < positive_integer_as_string:
        print("{0} time through loop.".format(loop_counter))
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
    