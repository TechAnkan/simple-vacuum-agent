from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target 

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Linear Regression using sklearn
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Sklearn Linear Regression:")
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Add bias term (intercept) manually
X_train_scaled_bias = np.concatenate((np.ones((X_train_scaled.shape[0], 1)), X_train_scaled), axis=1)
X_test_scaled_bias = np.concatenate((np.ones((X_test_scaled.shape[0], 1)), X_test_scaled), axis=1)

# Manual Linear Regression using normal equation
def linear_regression_model(X, y):
    weights = np.linalg.inv(X.T @ X) @ X.T @ y
    return weights

weights = linear_regression_model(X_train_scaled_bias, y_train)

# Predict using manual model
y_pred_manual = X_test_scaled_bias @ weights
mse_manual = mean_squared_error(y_test, y_pred_manual)
r2_manual = r2_score(y_test, y_pred_manual)

print("\nManual Linear Regression:")
print("Mean Squared Error (manual):", mse_manual)
print("R-squared (manual):", r2_manual)
