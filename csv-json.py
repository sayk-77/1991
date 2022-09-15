import csv
import json

with open('1991.csv', 'r', encoding='utf-8') as e:
    reader = csv.DictReader(e)
    rows = list(reader)

with open('1991.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f)
