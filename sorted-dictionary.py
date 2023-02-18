# Write output to a .csv file while sorting the rows according to value
# (Python 3.7+)

import csv

ProductMaster = { 1 : ["Minor Widget",0.25,250],
                  2 : ["Critical Widget",5.00,10],
                  3 : ["Complete System (Basic)",500,1],
                  4 : ["Complete System (Deluxe)",625,1]
                }

productReport = { 1 : [687500.0,11000,0.0],
                  2 : [250000.0,5000,12500.0],
                  3 : [1500000.0,3000,92500.0],
                  4 : [0,0,0]
                }

with open("c:/users/queen/documents/testexcel.csv", 'w') as file:

    csvWriter = csv.writer(file)

    csvWriter.writerow(["Name","GrossRevenue","TotalUnits","DiscountCost"])

    productKeys = ProductMaster.keys()

    # Used to sort the dictionary
    # reverse parameter set to True for descending order
    # Lambda used to specify the sort key, i.e. the first integer in the list of values
    # (side note: item[1][0] also works, but item[1] works because if item[1][0] is the same,
    # then item[1][1] will be compared as well)
    productReport = {k: v for k, v in sorted(productReport.items(), key=lambda item: item[1], reverse=True)}

    for key,value in productReport.items():

        if key in productKeys:

            csvWriter.writerow([ProductMaster[key][0], *value])

# file.close() isn't necessary when using with keyword
# with manages the file for you by creating a runtime context
# and discarding it after the with statement has ended.
