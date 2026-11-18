import csv
import numpy as np


def loadCsvToArray(path):
    rows = []

    csvFile = open(path, "r", newline="")
    reader = csv.reader(csvFile)

    for line in reader:
        if len(line) == 0:
            continue

        values = []
        for item in line:
            number = float(item)
            values.append(number)

        rows.append(values)

    csvFile.close()

    array = np.array(rows)
    return array

# MAIN
pathOpenFormat = "featureEmgOpenTest"
pathRestFormat = "featureEmgRestTest"
pathCloseFormat = "featureEmgTest"

arrayOfOpenData = []
arrayOfRestData = []
arrayOfCloseData = []

for i in range(10):
    tempMatrix = loadCsvToArray(pathOpenFormat + str(i+1) + ".csv")
    arrayOfOpenData.append(tempMatrix)

for i in range(10):
    tempMatrix = loadCsvToArray(pathRestFormat + str(i+1) + ".csv")
    arrayOfRestData.append(tempMatrix)

for i in range(10):
    tempMatrix = loadCsvToArray(pathCloseFormat + str(i+1) + ".csv")
    arrayOfCloseData.append(tempMatrix)


print(arrayOfOpenData)