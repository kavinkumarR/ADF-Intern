import csv
try:
    fi = open("test.csv", "r")
    reader = csv.reader(fi)
except:
    print("File not found")
else:
    dict1 = {x[0]: x[1:] for x in reader}
    print(dict1)