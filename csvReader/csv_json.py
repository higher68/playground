import csv
import json
name_list = []
with open("name.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_list.append(row)
for row in name_list:
    print(row)
    name_json_row = json.dumps(row)
    print(name_json_row)
name_json = json.dumps(name_list)
print(name_json)
