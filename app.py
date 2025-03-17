# coding: utf-8

import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load pre-trained model and column list
model = pickle.load(open("model.sav", "rb"))
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)


# Function to preprocess user input
def preprocess_input(df, model_columns):
    # List of categorical columns to encode
    categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
                        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 
                        'PaperlessBilling', 'PaymentMethod']
    
    # Convert numeric columns properly
    df['SeniorCitizen'] = pd.to_numeric(df['SeniorCitizen'], errors='coerce')
    df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
    df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # One-hot encode categorical columns
    df = pd.get_dummies(df, columns=categorical_cols)
    
    # Ensure all model columns are present, fill missing ones with 0
    df = df.reindex(columns=model_columns, fill_value=0)
    
    return df


# Route for homepage
@app.route("/")
def load_page():
    return render_template('home.html', query="")


# Route to handle form submission and make predictions
@app.route("/", methods=['POST'])
def predict():
    # Extract form inputs
    inputs = [request.form[f'query{i}'] for i in range(1, 20)]

    # Create DataFrame from input
    data = pd.DataFrame([inputs], columns=[
        'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 
        'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
        'InternetService', 'OnlineSecurity', 'OnlineBackup', 
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure'
    ])

    # Preprocess input data
    final_input = preprocess_input(data, model_columns)

    # Make prediction and get probability
    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0][1] * 100  # Convert to percentage

    # Prepare output messages
    if prediction == 1:
        o1 = "⚠️ This customer is likely to churn!"
    else:
        o1 = "✅ This customer is likely to stay."

    o2 = f"Confidence: {probability:.2f}%"

    # Render result back to form page
    return render_template(
        'home.html',
        output1=o1,
        output2=o2,
        **{f'query{i}': request.form[f'query{i}'] for i in range(1, 20)}
    )


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
