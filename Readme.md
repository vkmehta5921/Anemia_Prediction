
Final Project Report: AnemiaSense – Machine Learning for Anemia Detection
1. **Introduction**

1.1 ***Project Overview***

AnemiaSense is a machine learning-powered web application that aims to assist in the early detection of anemia. Anemia is a condition where the body lacks sufficient healthy red blood cells or hemoglobin, leading to fatigue and other health complications. Early detection is key to proper treatment and prevention of complications. AnemiaSense provides an accessible, efficient, and automated way to predict anemia using basic hematological parameters such as Hemoglobin, MCH, MCHC, and MCV.
1.2 Objectives
To design a machine learning model capable of detecting anemia with high accuracy.
To deploy the model within a simple, responsive Flask web application.
To make early anemia prediction accessible for educational or clinical demonstration purposes.

2. **Project Initialization and Planning Phase**

2.1 ***Define Problem Statement***

Anemia remains one of the most common health problems globally. Many individuals do not have easy access to healthcare or regular check-ups. Therefore, a lightweight, machine learning-based solution is proposed to identify anemia using only a few essential blood test results.

2.2 ***Project Proposal***

We propose a full-stack ML web application with the following flow:
Collect and clean data from open medical repositories.
Train a classification model.
Develop a web interface using Flask and HTML/CSS.
Host the solution locally or on cloud platforms.

2.3 ***Initial Planning***

Key technologies:
Language: Python
Frameworks: Flask, Scikit-learn
Front-end: HTML, CSS
Tools: Jupyter Notebook, GitHub, VS Code
Libraries: Pandas, NumPy, Seaborn, Matplotlib

3. **Data Collection and Preprocessing Phase**

3.1 ***Data Collection Plan***

Source: Kaggle dataset Iron Deficiency Anemia
Features: Gender, Hemoglobin, MCH, MCHC, MCV
Target: Result (0 = Normal, 1 = Anemia)

3.2 ***Data Quality Report***

Total entries: 1421
Missing values: None
Data types: Numeric (int64/float64)
Class balance: Slightly imbalanced
3.3 Preprocessing Steps
Converted gender into numeric (0: Female, 1: Male)
Normalized feature values
Split data into training and testing sets (80-20 split)

4. **Model Development Phase**

4.1 ***Feature Selection Report***

Correlation analysis showed strong relation of Hemoglobin, MCH, MCHC, and MCV with anemia status. These were selected as primary features.

4.2 ***Model Selection Report***

Models tested:
Logistic Regression
Decision Tree Classifier
Support Vector Machine
Random Forest Classifier (chosen for final deployment)
4.3 Training and Evaluation
Accuracy (Train/Test): 96% / 94 percent 
Metrics: Precision, Recall, F1-Score, Confusion Matrix
Random Forest showed best generalization and least overfitting

5. Model Optimization and Tuning Phase

5.1 ***Hyperparameter Tuning***

Used GridSearchCV to optimize parameters:
n_estimators: [100, 200]
max_depth: [None, 10, 20]
criterion: ["gini", "entropy"]
5.2 Metrics Comparison Report
Model
Accuracy Before
Accuracy After Tuning
Random Forest
93%
96%
Logistic Regression
85%
86%
SVM
88%
89%

5.3 ***Final Model Justification***
Random Forest was selected due to:
Strong performance
Better interpretability of feature importance
Robustness with default and tuned parameters

6. Results

6.1 ***Output Screenshots***

Input Form (index.html): Users enter values for Hemoglobin, MCH, MCHC, MCV.

Prediction Output (predict.html): Displays result with a success/failure message.


Screenshots show both UI/UX and backend success logs.



Final OutPut
               

7. Advantages & Disadvantages
Advantages
Lightweight application, deployable on low-resource systems
Uses minimal but essential features
Real-time prediction on the web
Disadvantages
Trained on a limited dataset
Not clinically certified (educational use)

8. Conclusion
AnemiaSense is a fully functional demonstration of how machine learning can be integrated with web technologies to solve real-life health problems. With 96 percent accuracy, it performs well as a proof-of-concept for remote anemia diagnosis support. It also showcases best practices in ML workflows, model validation, and UI development.

9. Future Scope
Integrate more features like RBC count, serum iron, ferritin
Add voice-based input
Deploy on cloud (e.g., Heroku, Render)
Integrate SMS/email alerts
Add multi-language support

10. Appendix
10.1 Source Code
All scripts (model training, Flask app, templates, forms) are available in the GitHub repository.
10.2 GitHub & Demo Link
GitHub: https://github.com/vkmehta5921/Anemia_Prediction
(Optional) Add YouTube demo or Render app if deployed.


 vivekmehta592001@gmail.com
 02/08/2025