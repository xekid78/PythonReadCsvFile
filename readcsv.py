for file in open("csv/sample.csv", "r"):
    line = file.rstrip().split(",")
    for data in line:
        print(data)
