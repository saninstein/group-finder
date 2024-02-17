"""
Converts csv file to json payload
"""
import json

delimiter = '_'
with open('names.csv') as source_file:
    items = source_file.read().split()


with open('payload.json', 'w') as json_file:
    json.dump(
        {'delimiter': delimiter, 'items': items},
        json_file,
        indent=4
    )
