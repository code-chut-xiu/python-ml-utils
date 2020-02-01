import numpy as np
from sklearn import preprocessing

# Create feature
feature = np.array([
    [-500.5],
    [-100.1],
    [0],
    [100.1],
    [900.9]
])
# Create scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Scale the feature
scaled_feature = minmax_scale.fit_transform(feature)

print(scaled_feature)

# Standardizing a feature
# Create a feature
x = np.array([
    [-1000.1],
    [-200.2],
    [500.5],
    [600.6],
    [9000.9]
])

# Create a scaler
scaler = preprocessing.StandardScaler()
# Transform the feature
standardized = scaler.fit_transform(x)
print(standardized)

# Robust Scaler
# Create a scaler
robust_scaler = preprocessing.RobustScaler()

# Transform feature
robust_scaled = robust_scaler.fit_transform(x)
print(robust_scaled)
