import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
# Make sure your CSV file is named 'data.csv' and is in the same folder
df = pd.read_csv('data.csv')

print("--- Original Data Preview ---")
print(df.head())

# 2. Clean Data: Fix Swapped Columns 
# (Based on the dataset where some rows have age and salary flipped, e.g., age > 100)
# We handle this conditionally if the 'Age' column accidentally contains a salary value.
if 'Age' in df.columns and 'Salary' in df.columns:
    # Convert columns to numeric, forcing errors to NaN
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    
    # If Age is unreasonably high (e.g., > 100), swap it with Salary
    swap_mask = df['Age'] > 100
    df.loc[swap_mask, ['Age', 'Salary']] = df.loc[swap_mask, ['Salary', 'Age']].values

# 3. Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# 4. Remove Duplicates
df = df.drop_duplicates()

print(f"\nCleaned Dataset Shape: {df.shape}")

# 5. Visualizations
sns.set_theme(style="whitegrid")

# Chart 1: Salary Distribution by Department
plt.figure(figsize=(8, 5))
sns.boxplot(x='Department', y='Salary', hue='Department', data=df, palette='Set2', legend=False)
plt.title('Salary Distribution Across Departments')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.tight_layout()
plt.savefig('salary_by_department.png') # Saves chart to your folder
if matplotlib.get_backend().lower() != 'agg':
    plt.show()

# Chart 2: Age vs Salary Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Salary', hue='Department', data=df, s=100, palette='viridis')
plt.title('Age vs. Salary Correlation')
plt.xlabel('Age')
plt.ylabel('Salary ($)')
plt.tight_layout()
plt.savefig('age_vs_salary.png') # Saves chart to your folder
if matplotlib.get_backend().lower() != 'agg':
    plt.show()

print("\nSuccess! Data cleaned and visual reports saved as PNG images.")