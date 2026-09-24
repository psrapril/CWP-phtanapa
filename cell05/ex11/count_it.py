#!/usr/bin/env python3

import sys

param = len(sys.argv[1:])

if param > 0:
    print(f"parameters: {param}")
    for i in range(param):
        print(f"{sys.argv[i + 1]}: {len(sys.argv[i + 1])}")
else:
    print("none")