import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
data = pd.read_csv('D:\\Practicals\\DATA SCIENCE\\DATA_SET.csv')

# ----------------------------- Simple Linear Regression -----------------------------
# Select independent and dependent variables
X_simple = data[['Cost']]
y_simple = data['Sales']

# Split data
X_train_simple, X_test_simple, y_train_simple, y_test_simple = train_test_split(
    X_simple, y_simple, test_size=0.2, random_state=42)

# Train model
model_simple = LinearRegression()
model_simple.fit(X_train_simple, y_train_simple)

# Predict
y_pred_simple = model_simple.predict(X_test_simple)

# Evaluate
print('Simple Linear Regression:')
print('Intercept:', model_simple.intercept_)
print('Coefficient:', model_simple.coef_)
print('Mean Squared Error (Simple):', mean_squared_error(y_test_simple, y_pred_simple))
print('R^2 Score (Simple):', r2_score(y_test_simple, y_pred_simple))
print()

# ----------------------------- Multiple Linear Regression -----------------------------
# Select variables
X_multiple = data[['Cost', 'Profit']]
y_multiple = data['Sales']

# Split data
X_train_multiple, X_test_multiple, y_train_multiple, y_test_multiple = train_test_split(
    X_multiple, y_multiple, test_size=0.2, random_state=42)

# Train model
model_multiple = LinearRegression()
model_multiple.fit(X_train_multiple, y_train_multiple)

# Predict
y_pred_multiple = model_multiple.predict(X_test_multiple)

# Evaluate
print('Multiple Linear Regression:')
print('Intercept:', model_multiple.intercept_)
print('Coefficients:', model_multiple.coef_)
print('Mean Squared Error (Multiple):', mean_squared_error(y_test_multiple, y_pred_multiple))
print('R^2 Score (Multiple):', r2_score(y_test_multiple, y_pred_multiple))

# ----------------------------- Visualization -----------------------------
# Simple Linear Regression Plot
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(X_test_simple, y_test_simple, color='blue', label='Actual')
plt.plot(X_test_simple, y_pred_simple, color='red', label='Predicted')
plt.title('Simple Linear Regression')
plt.xlabel('Cost')
plt.ylabel('Sales')
plt.legend()

# Multiple Linear Regression 3D Plot
fig = plt.figure(figsize=(14, 6))
ax = fig.add_subplot(122, projection='3d')
ax.scatter(X_test_multiple['Cost'], X_test_multiple['Profit'], y_test_multiple,
           color='blue', label='Actual')
ax.scatter(X_test_multiple['Cost'], X_test_multiple['Profit'], y_pred_multiple,
           color='red', label='Predicted')
ax.set_title('Multiple Linear Regression')
ax.set_xlabel('Cost')
ax.set_ylabel('Profit')
ax.set_zlabel('Sales')
ax.legend()

plt.tight_layout()
plt.show()
