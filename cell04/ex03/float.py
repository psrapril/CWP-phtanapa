#!/usr/bin/env python3
number_str = input("Give me a number: ")
number = float(number_str)

if number == int(number):
    print("This number is an integer.")
else:
    print("This number is a decimal.")