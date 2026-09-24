#!/usr/bin/env python3

import sys

param = sys.argv[1:]

if len(param) > 0:
    for text in param:
        if not text.endswith("ism"):
            print(f"{text}ism")
else:
    print("none")