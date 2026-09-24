#!/usr/bin/env python3

import sys

param = sys.argv[1:]

if len(param) == 2:
        result = list(range(int(param[0]), int(param[1]) + 1))
        print(result)
else:
    print("none")