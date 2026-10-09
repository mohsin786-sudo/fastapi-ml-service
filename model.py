import pandas as pd
from sklearn.linear_model import LogisticRegression 

data = {
      "age": [22, 25, 28, 30, 35, 40, 45],
      "salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000],
      "experience": [1, 2, 3, 5, 7, 10, 15],
      "target": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[[ "age", "salary", "experience"]]
y = df["target"]


model = LogisticRegression()

model.fit(X, y)
