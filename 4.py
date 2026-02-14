import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Create dataset
data = pd.DataFrame({
    'Study_Hours': [1, 2, 3, 4],
    'Sleep_Hours': [5, 6, 7, 8],
    'Marks': [50, 60, 70, 85]   # Target variable
})

# Separate features and target
X = data[['Study_Hours', 'Sleep_Hours']]
y = data['Marks']

# Step 4: Create interaction terms
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_interaction = poly.fit_transform(X)

# Get column names
columns = poly.get_feature_names_out(X.columns)
df_interaction = pd.DataFrame(X_interaction, columns=columns)

print("Interaction Data:")
print(df_interaction)

# Train Linear Regression model
model = LinearRegression()
model.fit(df_interaction, y)

print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict
predicted_marks = model.predict(df_interaction)
print("\nPredicted Marks:", predicted_marks)
