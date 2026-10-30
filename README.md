<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F4C2CF,100:D6718A&height=130&section=header&text=Employee%20Data%20Project&fontSize=34&fontColor=ffffff&fontAlignY=40" alt="Employee Data Project" />

**Cleaning a messy employee dataset, exploring it, predicting high earners and writing an HR analytics summary.**

![Python](https://img.shields.io/badge/Python-D6718A?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-D6718A?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-D6718A?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-D6718A?style=flat-square&logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-D6718A?style=flat-square&logo=plotly&logoColor=white)

</div>

---

## About

This repository holds my work for a data science internship. I worked on one messy employee dataset through four tasks: cleaning the data, exploring it, building a machine learning model, and putting everything into an HR analytics summary.

## Project files

| File | What it does |
|---|---|
| `data.csv` | The original raw dataset |
| `project.py` | Tasks 1 and 3: data cleaning and the main charts |
| `predictive_model.py` | Task 2: machine learning classification model |
| `eda_analysis.py` | Task 3: statistical data exploration |
| `capstone_analysis.py` | Task 4: final HR analytics report |
| `*.png` | Saved charts and report images |

## What I did

### Task 1: Data cleaning
- Fixed entry errors where `Age` and `Salary` values were swapped (for example, ages over 100).
- Filled missing numerical values with the **median**, so extreme values don't skew the data.
- Removed duplicate rows.

### Task 2: Predictive modeling
- Built a **Random Forest classifier** with scikit-learn to predict high-earning employees from age and department.
- Checked the model's accuracy and plotted a confusion matrix.

### Task 3: Exploratory data analysis
- Looked at descriptive statistics to find trends across departments.
- **IT has the highest pay variance, while Finance is much more consistent.**

### Task 4: Capstone HR analytics
- Combined the earlier work into a summary report on workforce distribution and payroll equity.

## Tech stack

Python · pandas · NumPy · Matplotlib · Seaborn · scikit-learn

## How to run

Make sure Python is installed, then run these in a terminal:

```bash
# 1. Clone the repo
git clone https://github.com/Meo-ow0/data_project.git
cd data_project

# 2. Install the packages
pip install pandas numpy matplotlib seaborn scikit-learn

# 3. Run the scripts in order
python project.py
python predictive_model.py
python eda_analysis.py
python capstone_analysis.py
```

The charts are saved as PNG files in the same folder.

## What I learned

- Real data is messy, and cleaning takes more time than modeling.
- The median is safer than the mean when a dataset has outliers.
- Accuracy alone doesn't tell the whole story, so I looked at the confusion matrix too.

## Contact

[LinkedIn](https://www.linkedin.com/in/shreya-8ab04536b/)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:D6718A,100:F4C2CF&height=80&section=footer" alt="" />

</div>
