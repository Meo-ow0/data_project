from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns

# 1. LOAD AND CLEAN DATASET (Carried over from Task 1)
data_path = Path(__file__).resolve().parent / "data.csv"
df = pd.read_csv(data_path)

# Clean swapped columns, missing values, and duplicates
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
swap_mask = df["Age"] > 100
df.loc[swap_mask, ["Age", "Salary"]] = df.loc[
    swap_mask, ["Salary", "Age"]
].values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df = df.drop_duplicates()

# 2. DEFINE TARGET VARIABLE & FEATURES
# Let's predict if an employee has a High Salary (> $75,000) -> 1 for Yes, 0 for No
df["High_Salary"] = (df["Salary"] > 75000).astype(int)

# Select features (Age and Department) and target (High_Salary)
X = df[["Age", "Department"]]
X = pd.get_dummies(X, drop_first=True)  # Convert text categories to numbers
y = df["High_Salary"]

# 3. TRAIN-TEST SPLIT (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. BUILD & TRAIN THE MODEL
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. MAKE PREDICTIONS & EVALUATE
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"--- Model Evaluation ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 6. VISUALIZE PERFORMANCE (Confusion Matrix)
plt.figure(figsize=(6, 4))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix - Salary Prediction Model")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()

# Save and show confusion matrix plot
plt.savefig("confusion_matrix.png")
print("\nSuccess! Confusion matrix saved as 'confusion_matrix.png'.")
plt.show()