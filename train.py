import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

X = []
y = []

for q in range(1,50):
    for h in range(24):
        X.append([q, h])
        y.append(q*2 + (h % 5))

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")