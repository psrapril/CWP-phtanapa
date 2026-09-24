#!/usr/bin/env python3

import sys

param = len(sys.argv[1:])

if param > 0:
   text = sys.argv[1]
   count_z = text.count("z")

   if count_z > 0:
        print("z" * count_z)
else:
    print("none")