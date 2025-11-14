# Electricity Theft Detection using Machine Learning

### AICTE Virtual Internship — Edunet Foundation

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Colab](https://img.shields.io/badge/Google%20Colab-Notebook-orange?logo=googlecolab)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-yellow?logo=scikitlearn)
![Status](https://img.shields.io/badge/Project%20Status-Completed-brightgreen)

---

## Overview

Electricity theft causes huge losses to utility companies and affects fair billing for consumers.  
This project applies machine learning techniques to detect suspicious electricity usage patterns that indicate theft.

The model is built using a Random Forest classifier. Severe class imbalance was handled using SMOTE, resulting in improved detection capability for theft cases.

---

## Objectives

- Detect fraudulent electricity consumption
- Analyze smart-meter energy patterns
- Balance dataset using SMOTE
- Improve recall for theft detection

---

## Project Structure

Electricity-Theft-Detection/
│
├── data/
│ └── electricity_theft_data.csv (or link to dataset)
│
├── notebook/
│ └── Electricity_Theft_Final.ipynb
│
├── model/
│ └── electricity_theft_model.pkl
│
├── screenshots/
│ ├── confusion_matrix.png
│ ├── feature_importance.png
│ └── output_report.png
│
├── README.md
└── requirements.txt

---

## Tech Stack

| Category  | Tools                                                              |
| --------- | ------------------------------------------------------------------ |
| Language  | Python                                                             |
| Platform  | Google Colab                                                       |
| Libraries | pandas, numpy, scikit-learn, matplotlib, seaborn, imblearn, joblib |
| Algorithm | Random Forest Classifier + SMOTE                                   |

---

## Model Performance

| Metric         | Score         |
| -------------- | ------------- |
| Accuracy       | ~90%          |
| Recall (Theft) | ~92%          |
| F1-Score       | ~91%          |
| Model          | Random Forest |

The recall improvement shows the model reliably identifies theft cases after SMOTE balancing.

---

## Visualizations

- Confusion Matrix
- Feature Importance Plot
- EDA Plots (Consumption Patterns)

Screenshots are in the `screenshots/` folder.

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Open Notebook
Run Electricity_Theft_Final.ipynb in Google Colab or Jupyter

# Model is saved as:
electricity_theft_model.pkl
```

Dataset

Smart-meter electricity consumption data.

Dataset Source (Kaggle):
(https://www.kaggle.com/datasets/sreen28g10/electricity-theft-detection)

Features

End-to-end ML pipeline
Data cleaning & preprocessing
Class imbalance handling (SMOTE)
Model training and evaluation
Feature importance analysis
Exported trained model (.pkl)
Future Scope
Deploy as web dashboard
Real-time anomaly detection
LSTM based consumption forecasting

Author

Dipika Mishra
AICTE × Edunet Foundation Virtual Internship — Artificial Intelligence

LinkedIn:(https://www.linkedin.com/in/dipika-mishra-24339625a/)
GitHub:(https://github.com/Dipika1226)
