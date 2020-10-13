import csv
import os

file_path = os.path.join("Resources/budget_data.csv")

with open(file_path, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    headers = next(csvreader)
    print(headers)

    # num_months = [0]

    for row in csvreader:
    
        dates = row[0]

        profit = row[1]

        # print(dates)

num_months = len(list("dates"))

print(num_months)

overall_profit = sum(f"profit")


    
#     for row in csvreader:
#         print(row)


# months= len(csvreader)

# print(months)

# months = (csvreader,1)
# print("There are: " + str(months) + "in this list."
# counter = 0
# for i in months:
#     counter = counter + 1

# print()
