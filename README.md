# 🚢 Titanic Analytics & Survival Intelligence Dashboard

An interactive Streamlit dashboard that explores the Titanic dataset through advanced visual analytics, business intelligence reporting, and machine learning-based survival prediction.

---

## 📌 Project Overview

The Titanic Analytics & Survival Intelligence Dashboard is a presentation-level Data Science project built using Streamlit, Plotly, and Machine Learning.

This dashboard transforms the famous Titanic dataset into an interactive business intelligence platform where users can:

- Explore passenger demographics
- Analyze survival patterns
- Discover key factors influencing survival
- Generate actionable insights
- Predict passenger survival probability using Machine Learning

The project demonstrates end-to-end Data Science workflow including data preprocessing, exploratory data analysis, feature engineering, visualization, dashboard development, and predictive modeling.

---

## 🎯 Project Objectives

- Perform Exploratory Data Analysis (EDA)
- Identify patterns affecting passenger survival
- Create interactive visualizations
- Build a machine learning prediction model
- Deploy a production-ready Streamlit dashboard

---

## ✨ Key Features

### 📊 Executive Dashboard

- Total Passengers
- Total Survivors
- Survival Rate
- Average Age
- Dynamic KPI Cards

### 🔍 Interactive Filters

Users can filter data by:

- Gender
- Passenger Class
- Age Range

All visualizations update dynamically based on selected filters.

### 📈 Visual Analytics

#### Survival Distribution

Analyze the percentage of passengers who survived and those who did not.

#### Age Distribution

Explore passenger age demographics and survival trends.

#### Gender Analysis

Compare survival rates between male and female passengers.

#### Passenger Class Analysis

Understand how travel class influenced survival probability.

#### Fare Analysis

Investigate the relationship between ticket fare and survival outcomes.

### 🤖 AI Insights

Automatically generated insights include:

- Female survival rate vs Male survival rate
- First-class survival rate vs Third-class survival rate
- Key factors contributing to passenger survival

### 🧠 Machine Learning Prediction

The dashboard includes a Random Forest Classification model that predicts survival probability based on:

- Passenger Class
- Gender
- Age
- Fare
- Family Size

Output includes:

- Survival Probability (%)
- Final Survival Prediction

### 📂 Dataset Explorer

- Interactive data table
- Real-time filtering
- Download filtered dataset as CSV

---

## 🛠️ Technology Stack

| Category | Tools |
|-----------|--------|
| Programming Language | Python |
| Dashboard Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Seaborn |
| Machine Learning | Scikit-Learn |
| Model | Random Forest Classifier |

---

## 📁 Project Structure

```text
Titanic-Dashboard/
│
├── titanic_dashboard.py
├── requirements.txt
├── README.md
│
└── assets/
    ├── dashboard.png
    └── screenshots/
```

---

## 📊 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Input Features

- Passenger Class
- Gender
- Age
- Fare
- Family Size

### Target Variable

- Survived (0 = No, 1 = Yes)

### Model Workflow

1. Data Cleaning
2. Missing Value Handling
3. Feature Engineering
4. Train-Test Split
5. Random Forest Training
6. Prediction & Probability Calculation

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/titanic-dashboard.git
```

### Navigate to Project Folder

```bash
cd titanic-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run titanic_dashboard.py
```

---

## 📈 Dashboard Sections

### Executive Dashboard

Provides high-level project KPIs and summary statistics.

### Analytics Dashboard

Contains interactive visualizations and exploratory analysis.

### AI Insights

Automatically highlights major findings from the dataset.

### Survival Predictor

Allows users to predict passenger survival probability using machine learning.

---

## 🎓 Skills Demonstrated

### Data Analysis

- Data Cleaning
- Feature Engineering
- Data Transformation

### Visualization

- Interactive Charts
- Dashboard Design
- Storytelling Through Data

### Machine Learning

- Classification
- Model Evaluation
- Predictive Analytics

### Deployment

- Streamlit Application Development
- GitHub Project Management

---

## 📸 Dashboard Preview

### Executive Overview

- Passenger KPIs
- Survival Distribution
- Age Distribution

### Analytics Section

- Survival by Gender
- Survival by Passenger Class
- Fare Analysis

### Prediction Module

- Passenger Survival Prediction
- Probability Score Generation

---

## 🌐 Live Demo

### Streamlit Dashboard

Add your deployed Streamlit URL here:

```text
https://your-streamlit-app.streamlit.app
```

---

## 📚 Dataset

Dataset Used:

Titanic Passenger Dataset from Seaborn

Source:

https://github.com/mwaskom/seaborn-data

---

## 👨‍💻 Author

### Harsh Raj

AI/ML | Machine Learning Engineer | Deep Learning Enthusiast

Interested in:

- Data Science
- Machine Learning
- Deep Learning
- Generative AI
- Analytics Engineering

---

## ⭐ If you found this project useful

Please consider giving the repository a star.

⭐ Star this repository to support future projects.
