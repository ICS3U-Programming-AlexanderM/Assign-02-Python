# !/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 1 2021
# This program asks for user input for the radius and
# units for a sphere.
# It then calculates and displays the volume and surface area.
import math
import colorama
from colorama import Fore


def main():
    # Set starting color
    print(Fore.BLUE + "")

    # Get user input
    print("This program calculates the volume and surface area of a sphere")
    print("")
    # Set variables with input
    unit = input(Fore.RED + "Enter the units: ")
    radius = int(input("Enter the radius ({}): ". format(unit)))
    decimal = int(input(
        "How many decimal places would you like the answer to be rounded to: "
        ))

    # Calculate variables
    volume = 4/3*math.pi*radius**3
    surface_area = 4*math.pi*radius**2

    # Round variables
    volume = round(volume, decimal)
    surface_area = round(surface_area, decimal)

    # Print variables
    print("")
    print(Fore.GREEN + "Volume = {} {}^3". format(volume, unit))
    print("Surface area = {} {}^2". format(surface_area, unit))


if __name__ == "__main__":
    main()
