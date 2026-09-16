# Employee Data Project - Internship Tasks

This repository contains my work for the data science internship project. I worked on a messy employee dataset to clean it up, run exploratory data analysis, build a machine learning model, and create an HR analytics summary.

## Project Files
- `data.csv` - The original raw dataset
- `project.py` - Task 1 & 3: Data cleaning and main charts
- `predictive_model.py` - Task 2: Machine learning classification model
- `eda_analysis.py` - Task 3: Statistical data exploration
- `capstone_analysis.py` - Task 4: Final HR analytics capstone report
- PNG files - Saved visual charts and reports

---

## What Was Done

### Task 1: Data Cleaning
- Fixed human-entry errors where `Age` and `Salary` values were swapped (e.g., unrealistic ages over 100).
- Filled in missing numerical values using medians to avoid skew.
- Removed duplicate rows to ensure clean data.

### Task 2: Predictive Modeling
- Built a Random Forest Classifier using `scikit-learn` to predict high-earning employees based on age and department.
- Evaluated model accuracy and generated a confusion matrix.

### Task 3: Exploratory Data Analysis (EDA)
- Analyzed descriptive statistics to find trends across departments.
- Discovered that the IT department has the highest pay variance, while Finance is much more consistent.

### Task 4: Capstone HR Analytics
- Put everything together into a summary report looking at workforce distribution and payroll equity.

---

## How to Run
Make sure Python is installed, install the required packages, and run the scripts from your terminal:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python project.py
python predictive_model.py
python eda_analysis.py
python capstone_analysis.py
