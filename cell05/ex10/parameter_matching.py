#!/usr/bin/env python3
import sys

param = sys.argv[1:]

if len(param) == 1:
    target = param[0]

    userinput = input("What was the parameter? ")

    if userinput == target:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")