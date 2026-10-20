import numpy as np

from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = load_iris()
X = iris.data      # numpy array
y = iris.target    # numpy array

lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

yHat = lda.predict(X)

for i in range(0, len(y)):
    if(yHat[i] != y[i]):
        print("Data Point #", i, "\tPredict: ", yHat[i], "\tReal", y[i])


print(lda.score(X, y))