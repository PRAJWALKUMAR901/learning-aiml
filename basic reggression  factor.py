import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
scores = np.array([50, 55, 65, 70, 75, 85])

model = LinearRegression()
model.fit(hours, scores)

predicted_marks=model.predict(hours)

print("scores = {:.2f}*hours + {:.2f} ".format(model.coef_[0],model.intercept_))

plt.scatter(hours, scores,label="scores",color="blue")
plt.plot(hours, predicted_marks,label="predicted marks",color="red")
plt.xlabel("hours")
plt.ylabel("scores")
plt.legend()
plt.grid(True)
plt.show()

