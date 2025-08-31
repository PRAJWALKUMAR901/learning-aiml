import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





ds = pd.read_csv('car.csv')
x = ds.iloc[:, :-1].values
y = ds.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)

print("MILEAGE for Engine=5L, Weight=2000kg:", lr.predict(ss.transform([[5,2000]]))[0])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter (raw features, actual values)
ax.scatter(x[:,0], x[:,1], y, color='red', label='Actual data')

# Surface (model predictions)
x_surf, y_surf = np.meshgrid(
    np.linspace(x[:,0].min(), x[:,0].max(), 100),
    np.linspace(x[:,1].min(), x[:,1].max(), 100)
)
xy_scaled = ss.transform(np.column_stack([x_surf.ravel(), y_surf.ravel()]))  # scale meshgrid
z_surf = lr.predict(xy_scaled).reshape(x_surf.shape)

ax.plot_surface(x_surf, y_surf, z_surf, color='blue', alpha=0.5, label='Regression plane')

# Labels
ax.set_xlabel('ENGINE SIZE (liters)')
ax.set_ylabel('CAR WEIGHT (kg)')
ax.set_zlabel('MILEAGE (km/l)')
ax.legend()
plt.show()


