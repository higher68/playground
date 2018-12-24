import csv
keys = ["firesname", "secondname"]
name_list = []
with open("name_nohead.csv", "r") as f:
    reader = csv.DictReader(f, fieldnames=keys)
    for row in reader:
        name_list.append(row)

for row in name_list:
    print(row)

