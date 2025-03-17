
# 📊 Telecom Customer Churn Prediction

Welcome to the **Telecom Customer Churn Prediction** project!  
This end-to-end machine learning pipeline analyzes customer behavior to predict which customers are likely to stop using telecom services (churn). The system includes **data exploration, model training, and web deployment** to demonstrate how machine learning can be applied in real-world business scenarios.

---

## 🚀 Project Overview

This project focuses on identifying the key reasons behind customer churn in a telecom company. The approach covers:
- **Exploratory Data Analysis (EDA)** to understand data patterns.
- **Feature Engineering and Preprocessing** for model readiness.
- **Model Training** using advanced techniques to handle class imbalance.
- **Deployment** via Flask web application, making predictions interactive and accessible.

---

## ✅ Key Components

### 1. 📈 Exploratory Data Analysis (EDA)

In the EDA phase, we analyzed customer demographics, service usage, and billing data to identify trends and factors leading to churn. Visualization techniques and summary statistics were used to uncover insights such as:
- Which service categories are highly correlated with churn.
- Customer tenure and payment patterns affecting retention.
- Identification of outliers and missing data handling.


---

### 2. ⚙️ Model Building and Training

We employed advanced models such as **Decision Trees** and **SMOTEENN (for balancing)** to create a churn prediction model. To ensure accuracy:
- Categorical variables were encoded properly.
- Imbalanced classes were handled using **SMOTEENN**, a combination of SMOTE and Edited Nearest Neighbors.
- Hyperparameters were tuned to improve model performance.


**Key Highlights:**
- Handling of imbalanced data.
- Use of Decision Tree Classifier.
- Saving trained model using Pickle (`model.sav`).
- Extracting and storing model feature columns (`model_columns.pkl`).

---

### 3. 🌐 Model Deployment with Flask

The trained model is deployed using a Flask web application that allows users to enter customer details and get churn predictions in real-time.

**Key Features of Flask App:**
- A user-friendly web interface built with HTML and Bootstrap.
- Handles POST requests to predict churn.
- Displays prediction result with confidence score.

📄 **File**: `app.py`

---

## 🌍 Live Demo & Usage

Upon deploying this project (e.g., on Render or Railway), users can visit the web app, fill in customer data, and predict if the customer is likely to churn.

### 🧭 Sample Workflow:
1. Open the web app.
2. Fill customer attributes (e.g., gender, monthly charges, contract type).
3. Submit the form.
4. See the prediction output:
   - **Likely to churn** or **Likely to stay**.
   - Confidence percentage.

---

## 🛠️ Technologies & Libraries Used

- **Python 3.x**
- **Pandas** — for data manipulation.
- **NumPy** — for numerical operations.
- **Scikit-learn** — for machine learning models.
- **Imbalanced-learn** — for handling class imbalance.
- **Flask** — for building and deploying web application.
- **Bootstrap** — for frontend styling.

---


## ✨ Conclusion

This project demonstrates a **complete machine learning workflow** from analysis to deployment, giving insights into customer behavior and enabling companies to proactively prevent churn.  
By leveraging **model insights and interactive prediction**, this solution helps businesses make informed retention strategies.

---


## 🌐 Live App

👉 [Check out the Live Churn Prediction App](https://telecom-churn-model.onrender.com/)

---

## 🔗 Connect with Me

- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/sourav-kumar-30141b174)
- **X (Twitter)**: [Your X (Twitter) Profile](https://x.com/souravkumarr73)

---

