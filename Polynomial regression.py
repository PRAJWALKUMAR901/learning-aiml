import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds=pd.read_csv('car_price_poly.csv')

x=ds.iloc[1:,0].values.reshape(-1,1)
y=ds.iloc[1:,1].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
ss_x=StandardScaler()
ss_y=StandardScaler()
x=ss_x.fit_transform(x)
y=ss_y.fit_transform(y)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=4)
lr=LinearRegression()
x_poly=poly.fit_transform(x)
lr.fit(x_poly,y)

plt.scatter(ss_x.inverse_transform(x),ss_y.inverse_transform(y),color='red')
plt.plot(ss_x.inverse_transform(x),ss_y.inverse_transform(lr.predict(x_poly)),color='blue')
plt.show()

print('The price for 7.5year old car is $',ss_y.inverse_transform(lr.predict(poly.fit_transform(ss_x.transform([[7.5]])))))









