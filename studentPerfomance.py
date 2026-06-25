import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# -----------------------------------
# STEP 1: Create Dataset
# -----------------------------------
data = {
    'Hours': [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    'Scores': [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]
}

df = pd.DataFrame(data)

print("DATASET")
print(df)

# -----------------------------------
# STEP 2: Summary Statistics
# -----------------------------------
print("\nSUMMARY STATISTICS")
print(df.describe())

# -----------------------------------
# STEP 3: Check Missing Values
# -----------------------------------
print("\nMISSING VALUES")
print(df.isnull().sum())

# Handle missing values if any
df = df.dropna()

# -----------------------------------
# STEP 4: Scatter Plot
# -----------------------------------
plt.scatter(df['Hours'], df['Scores'])
plt.title("Study Hours vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()

# -----------------------------------
# STEP 5: Split Dataset
# -----------------------------------
X = df[['Hours']]
y = df['Scores']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------
# STEP 6: Train Linear Regression
# -----------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------------
# STEP 7: Predict Score for 6.5 Hours
# -----------------------------------
hours = np.array([[6.5]])

predicted_score = model.predict(hours)

print("\nPREDICTION")
print(f"Predicted Score for 6.5 study hours: {predicted_score[0]:.2f}")

# -----------------------------------
# STEP 8: Predicted Scores and Error
# -----------------------------------
df['Predicted Score'] = model.predict(X)

df['Error'] = df['Scores'] - df['Predicted Score']

print("\nDATAFRAME WITH ERRORS")
print(df)

# -----------------------------------
# STEP 9: Regression Line
# -----------------------------------
plt.scatter(df['Hours'], df['Scores'], label='Actual Scores')
plt.plot(df['Hours'],
         df['Predicted Score'],
         label='Regression Line')

plt.title("Study Hours vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.legend()
plt.show()

# -----------------------------------
# STEP 10: Actual vs Predicted Plot
# -----------------------------------
plt.scatter(df['Hours'],
            df['Scores'],
            label='Actual Scores')

plt.scatter(df['Hours'],
            df['Predicted Score'],
            label='Predicted Scores')

plt.title("Study Hours vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.legend()
plt.show()

# -----------------------------------
# STEP 11: Multivariate Regression
# -----------------------------------
df['Practice_Exams'] = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4]

print("\nUPDATED DATAFRAME")
print(df[['Hours', 'Practice_Exams', 'Scores']])

X_multi = df[['Hours', 'Practice_Exams']]
y_multi = df['Scores']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

multi_model = LinearRegression()
multi_model.fit(X_train_m, y_train_m)

prediction_multi = multi_model.predict([[6.5, 3]])

print("\nMULTIVARIATE PREDICTION")
print(f"Predicted Score for 6.5 hours and 3 practice exams: {prediction_multi[0]:.2f}")

# -----------------------------------
# STEP 12: Evaluate Model
# -----------------------------------
y_pred_test = multi_model.predict(X_test_m)

comparison = pd.DataFrame({
    'Actual': y_test_m,
    'Predicted': y_pred_test
})

print("\nACTUAL VS PREDICTED")
print(comparison)

mae = mean_absolute_error(y_test_m, y_pred_test)
mse = mean_squared_error(y_test_m, y_pred_test)

print("\nMODEL EVALUATION")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)

# -----------------------------------
# STEP 13: User Input Function
# -----------------------------------
def predict_score():
    hours = float(input("\nEnter study hours: "))
    prediction = model.predict([[hours]])
    print(f"Predicted Score: {prediction[0]:.2f}")

predict_score()