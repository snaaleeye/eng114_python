import csv


with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(list(csvreader))


    # print(csvreader)

    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    #
    # for row in csvreader:
    #     print(row[-1])