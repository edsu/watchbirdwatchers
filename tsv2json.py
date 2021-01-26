#!/usr/bin/env python3

import csv
import sys
import json
import fileinput

objects = []

for row in csv.DictReader(fileinput.input()):
    obj = {}
    for key, val in row.items():
        obj[key] = val
    objects.append(obj)

print(json.dumps(objects, indent=2))

