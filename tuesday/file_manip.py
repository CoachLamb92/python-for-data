import csv

rows = []

with open("tuesday/employees.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)
    for row in csvreader:
        rows.append(row)

# print(headers)
# print(rows)

header = ["Name", "Age"]
data = [
    ["Alex", 25],
    ["Brad", 45],
    ["Joey", 18]
    ]

with open("tuesday/student_info.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)


with open("tuesday/employees.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open("tuesday/student_info_2.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for el in data:
        writer.writerow({"Name": el[0], "Age": el[1]})