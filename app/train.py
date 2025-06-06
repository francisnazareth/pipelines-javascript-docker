import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Reading the data
iris = pd.read_csv("iris.csv")
print(iris.head())
y = iris['Species']
iris.drop(columns='Species', inplace=True)
x = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# Training the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = LogisticRegression(max_iter=100)
model.fit(x_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))