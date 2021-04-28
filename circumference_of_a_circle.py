#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program calculates the circumference of a circle
#    with radius inputted from the user

import constants


def main():
    # This function calculates the circumference of a circle

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = radius * constants.TAU

    # output
    print("circumference is {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
