# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.datasets import fetch_california_housing
# import numpy as np

# data = fetch_california_housing()
# X = data.data
# y = data.target 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# x_test_scaled = scaler.transform(X_test)

# model = LinearRegression()
# model.fit(X_train_scaled, y_train) 

# y_pred = model.predict(x_test_scaled)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R-squared:", r2)
# # The code above implements a linear regression model on the California housing dataset.

# X_train_scaled = np.concatenate((np.ones((X_train.shape[0], 1)), X_train_scaled), axis=1)
# X_test_scaled = np.concatenate((np.ones((X_test.shape[0], 1)), X_test_scaled), axis=1)
# # It includes data preprocessing with standard scaling, fitting the model, and evaluating its performance using mean

# def linear_regression_model():
#    weights = np.linalg.inv(X.T @ X) @ X.T @ y
#    return weights
# weights = linear_regression_model(X_train_scaled, y_train)
# print("Weights from manual linear regression:", weights)
# y_pred = X_test_scaled @ weights 
# mse_manual = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error (manual):", mse_manual)
# print("R-squared (manual):", r2) 
# # The manual implementation of linear regression calculates the weights using the normal equation.