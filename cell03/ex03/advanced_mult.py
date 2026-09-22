#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

count = 0
while count <= 10:
    print(f"Table de {count}: ", end="")

    number = 0
    while number <= 10:
        print(f" {count * number}", end="")
        number += 1
    print()
    count += 1