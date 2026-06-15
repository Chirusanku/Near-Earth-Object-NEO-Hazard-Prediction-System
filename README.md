# 🚀 Near-Earth Object (NEO) Hazard Prediction System

## 📌 Project Overview

The **Near-Earth Object (NEO) Hazard Prediction System** is a Machine Learning project developed to predict whether a Near-Earth Object (asteroid) is hazardous to Earth based on its physical and orbital characteristics.

This project leverages data preprocessing, feature engineering, model training, hyperparameter tuning, and deployment techniques to build an end-to-end predictive system that assists in identifying potentially dangerous asteroids.

---

## 🎯 Objective

To develop a Machine Learning model capable of accurately classifying Near-Earth Objects (NEOs) as **Hazardous** or **Non-Hazardous** using historical asteroid data.

---

## 💼 Business Problem

Space agencies such as NASA continuously monitor thousands of asteroids. Manually analyzing every object is time-consuming and resource-intensive.

This project aims to:

* Automate hazard prediction.
* Assist researchers in prioritizing high-risk asteroids.
* Improve early warning systems.
* Support decision-making for planetary defense initiatives.

---

## 📊 Dataset Information

The dataset contains information about Near-Earth Objects, including:

### Features

* Absolute Magnitude
* Estimated Diameter (Minimum)
* Estimated Diameter (Maximum)
* Relative Velocity
* Miss Distance
* Orbiting Body
* Sentry Object Status
* Other orbital parameters

### Target Variable

* **is_hazardous**

  * 1 → Hazardous
  * 0 → Non-Hazardous

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit
* Jupyter Notebook

---

## 📂 Project Structure

```text
NEO-Hazard-Prediction-System/
│
├── data/
│   └── neo.csv
│
├── notebooks/
│   └── NEO_Hazard_Prediction.ipynb
│
├── models/
│   └── model.pkl
│
├── app.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── confusion_matrix.png
    ├── roc_curve.png
    └── feature_importance.png
```

---

## 🔄 Project Workflow

### Sprint 1 – Data Collection & Understanding

* Dataset acquisition
* Exploratory Data Analysis (EDA)
* Understanding feature distributions
* Identifying missing values

### Sprint 2 – Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Feature scaling
* Outlier analysis

### Sprint 3 – Model Building & Optimization

* Train-Test Split
* Model Training
* Hyperparameter Tuning
* Performance Evaluation

Algorithms explored:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors
* Support Vector Machine
* Gradient Boosting

### Sprint 4 – End-to-End Pipeline & Deployment

* Pipeline creation
* Model serialization using Joblib/Pickle
* Streamlit application development
* Prediction interface deployment

---

## 📈 Machine Learning Pipeline

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Encoding
   ↓
Feature Scaling
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Deployment
```

---

## 📊 Evaluation Metrics

The model performance is evaluated using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC Score

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/NEO-Hazard-Prediction-System.git
```

### Navigate to Project Folder

```bash
cd NEO-Hazard-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 📷 Application Features

* User-friendly interface
* Real-time hazard prediction
* Instant classification results
* End-to-end ML pipeline integration
* Easy deployment and scalability

---

## 📌 Results

The developed model successfully predicts hazardous asteroids using orbital and physical characteristics, helping automate the identification process and improving space-object monitoring efficiency.

---

## 🔮 Future Enhancements

* Deep Learning implementation
* Real-time NASA API integration
* Cloud deployment (AWS/Azure)
* Interactive dashboards
* Automated model retraining

---

## 👨‍💻 Author

**Sanku Chiru V.N.S.S. Vara Prasad**

* Electronics and Communication Engineering (ECE)
* Data Science & Machine Learning Enthusiast
* Passionate about AI, Analytics, and Predictive Modeling

---

## 🙏 Acknowledgements

* NASA for providing asteroid-related data.
* Open-source Python community.
* Scikit-Learn development team.

⭐ If you found this project useful, consider giving it a star on GitHub!
