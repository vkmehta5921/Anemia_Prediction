import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Dummy input (replace values with real ones if needed)
# Example: [Hemoglobin, MCH, MCHC, MCV]
test_input = np.array([[12.5, 27.3, 33.2, 80.0]])

# Predict
try:
    result = model.predict(test_input)
    print("Prediction output:", result)
except Exception as e:
    print("Error during prediction:", e)
