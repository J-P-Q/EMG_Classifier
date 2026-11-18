from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
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
classes = ["Open", "Rest", ""]


for heldOutBatch in range(1, 11):
    trainRows = []
    trainLabels = []
    testRows = []
    testLabels = []
    for className in classes:
        for holdNumber in range(1, 11):
            path = "featureEmg" + className + "Test" + str(holdNumber) + ".csv"
            #print("Path: ", path)
            fileArray = loadCsvToArray(path)

            for row in fileArray:
                if holdNumber == heldOutBatch:
                    testRows.append(row)
                    testLabels.append(className)
                else:
                    trainRows.append(row)
                    trainLabels.append(className)

    Xtrain = np.array(trainRows)
    Xtest = np.array(testRows)

    lda = LinearDiscriminantAnalysis()
    lda.fit(Xtrain, trainLabels)

    print("Accuracy", heldOutBatch, ":  ", lda.score(Xtest, testLabels))

