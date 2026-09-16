import matplotlib

matplotlib.use(
    "Agg"
)  # Safe backend for saving plots without popping up windows
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. LOAD AND CLEAN DATASET
df = pd.read_csv("data.csv")

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

print("--- Statistical Summary of Cleaned Data ---")
print(df.describe())

print("\n--- Department-wise Salary Breakdown (Mean & Median) ---")
dept_stats = (
    df.groupby("Department")["Salary"]
    .agg(["count", "mean", "median", "std"])
    .reset_index()
)
print(dept_stats)

# 2. GENERATE ADVANCED EDA VISUALIZATIONS
sns.set_theme(style="whitegrid")

# Visualization 1: Violin Plot (Distribution & Density across Departments)
plt.figure(figsize=(9, 5))
sns.violinplot(
    data=df, x="Department", y="Salary", palette="Set2", inner="quartile"
)
plt.title(
    "EDA: Salary Density and Quartile Distribution by Department",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Department")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.savefig("eda_salary_violin.png")
print("\nSaved: eda_salary_violin.png")

# Visualization 2: Pairplot or Correlation Heatmap for Numerical Insights
plt.figure(figsize=(7, 5))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(
    numeric_df.corr(), annot=True, cmap="Blues", fmt=".2f", linewidths=1
)
plt.title(
    "EDA: Feature Correlation Heatmap", fontsize=12, fontweight="bold"
)
plt.tight_layout()
plt.savefig("eda_correlation_heatmap.png")
print("Saved: eda_correlation_heatmap.png")