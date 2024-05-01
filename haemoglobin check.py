import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from Excel
file_path = r'C:\Users\vedansh\Desktop\Python Dev Hemoglobin Data.xlsx'
data = pd.read_excel(file_path)

# Extract features and target variable
X = data.drop(columns=['hbvalues', 'image_name', 'model'])
y = data['hbvalues']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Accept input from the user for features
print("Enter the features for prediction:")
features = {}
for column in X.columns:
    value = float(input(f"Enter value for {column}: "))
    features[column] = value

# Convert features to a DataFrame for prediction
input_data = pd.DataFrame([features])

# Predict hemoglobin value
prediction = model.predict(input_data)[0]

print("Predicted Hemoglobin Value:", prediction)
