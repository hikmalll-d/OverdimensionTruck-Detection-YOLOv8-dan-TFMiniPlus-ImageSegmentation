import numpy as np
from sklearn.linear_model import LinearRegression

distance = np.array([8,9,10]).reshape(-1,1)

scale = np.array([0.83,0.93,1.04])

model = LinearRegression()

model.fit(distance, scale)

a = model.coef_[0]
b = model.intercept_

print("scale =",a,"* distance +",b)