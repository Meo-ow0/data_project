Employee Data Cleaning & Visualization Project
This is a data preprocessing and exploratory data analysis (EDA) project completed as part of my internship. The goal was to take a messy, raw dataset containing employee records, clean up inconsistencies, handle structural errors, and build visualizations to uncover insights.

Project Structure
Plaintext
├── data.csv                 # Raw, uncleaned dataset
├── project.py               # Main Python script for cleaning and analysis
├── cleaned_data.csv         # Processed and cleaned dataset (generated upon running)
├── salary_by_department.png # Box plot visualizing salary distribution
└── age_vs_salary.png        # Scatter plot analyzing age vs. salary trends
What I Did (Data Cleaning Pipeline)
Real-world data is rarely clean. In this project, I handled several common data quality issues inside project.py:

Fixed Swapped Columns: Identified rows where human entry error caused Age and Salary values to swap (e.g., ages over 100), and programmatically flipped them back.

Missing Value Imputation: Handled missing values in critical numeric columns (Age, Salary) using the median value to prevent skewness from outliers.

Duplicate Removal: Dropped exact duplicate records to ensure data integrity.

Key Visualizations & Insights
Salary Distribution (salary_by_department.png): A box plot comparing salaries across HR, Finance, and IT. It highlights median salaries per department while clearly exposing high-end compensation outliers.

Age vs. Salary Correlation (age_vs_salary.png): A color-coded scatter plot broken down by department to see if age/experience correlates with salary progression.

How to Run This Project
Make sure you have Python installed along with the required libraries, then follow these steps:

Clone or download this repository into your local folder.

Install dependencies via terminal:

Bash
pip install pandas matplotlib seaborn
Run the analysis script:

Bash
python project.py
Check your folder for the newly generated charts (.png files) and the cleaned dataset.
