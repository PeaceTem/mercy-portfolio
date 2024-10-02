import joblib
import numpy as np
import pandas as pd
# Load the model from the file
loaded_rf_model = joblib.load('random_forest_model.pkl')

feature_names = ['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Tutoring_Sessions', 'Physical_Activity', 'Previous_cgpa', 'Access_to_Resources_Encoded', 'Motivation_Level_Encoded', 'Family_Income_Encoded', 'Teacher_Quality_Encoded', 'School_Type_Encoded', 'Peer_Influence_Encoded', 'Parental_Education_Level_Encoded', 'Distance_from_Home_Encoded', 'Gender_Encoded', 'Parental_Involvement_Encoded', 'Extracurricular_Activities_Encoded', 'Internet_Access_Encoded', 'Learning_Disabilities_Encoded']
X_test_manual = pd.DataFrame([[5, 24, 10, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0]], columns=feature_names) # reduce score to 0 to 1
# Now you can use the loaded model
predictions = loaded_rf_model.predict(X_test_manual)
print(predictions)