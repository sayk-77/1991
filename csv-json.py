import csv
import json

with open('1991.csv') as e:
    reader = csv.DictReader(e)
    rows = list(reader)

with open('1991.json', 'w') as f:
    json.dump(rows, f)