import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")

test_input = np.array([[15]])
prediction = model.predict(test_input)

print("Input:", test_input[0][0])
print("Predicted output:", prediction[0])
print("Model saved as model.pkl")
