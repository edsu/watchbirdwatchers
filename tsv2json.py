#!/usr/bin/env python3

import sys
import json
import fileinput

cols = None
objects = []

for line in fileinput.input():
    row = line.split("\t")
    if not cols:
        cols = row
    else:
        objects.append(dict(zip(cols, row)))

print(json.dumps(objects, indent=2))

