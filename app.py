#app.py

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load feature names
try:
    features = pickle.load(open('feature_columns.pkl', 'rb'))
except:
    features = ['Hemoglobin', 'MCH', 'MCHC', 'MCV']  # fallback

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        input_values = [float(request.form.get(feature)) for feature in features]
        input_array = np.array([input_values])  # 2D array for model

        # Predict using loaded model
        prediction = model.predict(input_array)[0]

        # Interpretation
        result = "Anemia Detected (High Risk)" if prediction == 1 else "No Anemia Detected (Normal)"
        return render_template('predict.html', prediction_text=result)

    except Exception as e:
        return render_template('predict.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
