from flask import Flask, render_template, request, redirect
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load feature column names (if available)
try:
    features = pickle.load(open('feature_columns.pkl', 'rb'))
except:
    features = ['Hemoglobin', 'MCH', 'MCHC', 'MCV']  # fallback default

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values from the form
        input_values = []
        for feature in features:
            value = request.form.get(feature)
            if value is None or value.strip() == "":
                raise ValueError(f"{feature} is required.")
            input_values.append(float(value))

        # Create DataFrame to avoid sklearn warning
        input_df = pd.DataFrame([input_values], columns=features)

        # Make prediction
        prediction = model.predict(input_df)[0]
        result = "🩸 Anemia Detected (High Risk)" if prediction == 1 else "✅ No Anemia Detected (Normal)"

        return render_template('predict.html', prediction_text=result)

    except Exception as e:
        return render_template('predict.html', prediction_text=f"Error: {str(e)}")

@app.errorhandler(405)
def method_not_allowed(e):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
