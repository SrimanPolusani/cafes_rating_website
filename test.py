import csv

list_rows = []
with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')  # Here the delimiter is "," (Comma Separated Values)
    for row in csv_data:
        list_rows.append(row)
        print(row)