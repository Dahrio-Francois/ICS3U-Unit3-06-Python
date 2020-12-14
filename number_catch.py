#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: Dahrio Francois
# this program is a number guessing game
#     that catches string

import random
some_variable = random.randint(1, 20)  # a number between 1 & 20


def main():
    # this function catches string in a number guessing game

    # input
    integer_as_string = input("Enter an integer: ")
    print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly!")
    except Exception:
        print("This was not an integer")
    else:
        if integer_as_number == some_variable:
            print("Correct")

        elif integer_as_number > some_variable:
            print("Incorrect. Too high!")
            print(some_variable)

        elif integer_as_number < some_variable:
            print("Incorrect, Too low!")
            print(some_variable)


if __name__ == "__main__":
    main()
