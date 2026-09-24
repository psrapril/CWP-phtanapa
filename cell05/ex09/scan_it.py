#!/usr/bin/env python3
import sys
import re

param = sys.argv[1:]

if len(param) == 2:
    keyword = param[0]
    text = param[1]

    matches = re.findall(re.escape(keyword), text)
    count = len(matches)

    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")