import csv

name_list = []
with open("name.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_list.append(row)

for row in name_list:
    print(row)

