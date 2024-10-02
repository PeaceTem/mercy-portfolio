from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import joblib
import json
import os
import numpy as np
import pandas as pd
from .utils import calc_cgpa, family_income, Learning_Disabilities
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Load your saved Random Forest model (assume it's in the project directory)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'random_forest_model.pkl')
model = joblib.load(MODEL_PATH)




@method_decorator(csrf_exempt, name='dispatch')
class PredictView(View):
    def get(self, request):
        """
        Handles the GET request.
        Displays an HTML page with information on how to use the POST request for predictions.
        """
        context = {
            'info': 'To make a prediction, send a POST request with the following format: {"feature1": value, "feature2": value, ...}'
        }
        return render(request, 'api/predict_info.html', context)
    


    # use a function-based view
    # @csrf_exempt
    def post(self, request):
        """
        Handles the POST request.
        Extracts data from the request, uses the saved Random Forest model to make a prediction, and returns the result.
        """
        try:
            # Get the input data from the POST request
            # print(request.POST.items())

            for key, value in request.POST.items():
                print(f"{key}: {value}")
            data = self.request.POST.dict()  # if form data is used
            # print(data)
            # Alternatively, if you are expecting JSON data, use:
            # import json
            # data = json.loads(request.body)

            feature_names = ['Hours_Studied',
                            'Attendance',
                            'Sleep_Hours', 
                            'Tutoring_Sessions', 
                            'Physical_Activity', 
                            'Previous_cgpa', 
                            'Access_to_Resources_Encoded', 
                            'Motivation_Level_Encoded', 
                            'Family_Income_Encoded', 
                            'Teacher_Quality_Encoded', 
                            'School_Type_Encoded', 
                            'Peer_Influence_Encoded', 
                            'Parental_Education_Level_Encoded', 
                            'Distance_from_Home_Encoded', 
                            'Gender_Encoded', 
                            'Parental_Involvement_Encoded', 
                            'Extracurricular_Activities_Encoded', 
                            'Internet_Access_Encoded', 
                            'Learning_Disabilities_Encoded']
            

            # Convert data to the appropriate format (e.g., list or numpy array)
            # Assuming the data contains feature1, feature2, etc. and matches model's expected input
            input_data = np.array([[
                int(data['Hours_Studied']), #
                int(data['Attendance']), #
                int(data['Sleep_Hours']), #
                1,
                1,
                calc_cgpa(data['Previous_cgpa']), #
                2, 
                2,
                family_income(data['Family_Income']), #Low: 1, Medium: 2, High: 0
                1,
                1,
                2,
                0,
                2,
                0,
                0,
                1,
                1,
                Learning_Disabilities(data['Learning_Disabilities']), # No: 0, Yes: 1

                # Add more features as required
            ]])

            X_test_manual = pd.DataFrame(input_data, columns=feature_names) # reduce score to 0 to 1
            # Use the model to make a prediction
            prediction = model.predict(X_test_manual)

            # Return the prediction as JSON response
            return JsonResponse({'prediction': prediction[0]})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)




@csrf_exempt
def my_json_view(request):
    if request.method == 'POST':
        # Get JSON data from the request body
        try:
            data = json.loads(request.body)

            input_data = [[
                int(data.get('Hours_Studied', '10')), #

                int(data.get('Attendance', '75')), #
                int(data.get('Sleep_Hours', '7')), #
                1,
                1,
                calc_cgpa(data.get('Previous_cgpa', '75')), #
                2, 
                2,
                family_income(data.get('Family_Income', 'Medium')), #Low: 1, Medium: 2, High: 0
                1,
                1,
                2,
                0,
                2,
                0,
                0,
                1,
                1,
                Learning_Disabilities(data.get('Learning_Disabilities', 'No')), # No: 0, Yes: 1
                # Add more features as required
            ]]

            feature_names = ['Hours_Studied',
                            'Attendance',
                            'Sleep_Hours', 
                            'Tutoring_Sessions', 
                            'Physical_Activity', 
                            'Previous_cgpa', 
                            'Access_to_Resources_Encoded', 
                            'Motivation_Level_Encoded', 
                            'Family_Income_Encoded', 
                            'Teacher_Quality_Encoded', 
                            'School_Type_Encoded', 
                            'Peer_Influence_Encoded', 
                            'Parental_Education_Level_Encoded', 
                            'Distance_from_Home_Encoded', 
                            'Gender_Encoded', 
                            'Parental_Involvement_Encoded', 
                            'Extracurricular_Activities_Encoded', 
                            'Internet_Access_Encoded', 
                            'Learning_Disabilities_Encoded']
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        

        
        X_test_manual = pd.DataFrame(input_data, columns=feature_names) # reduce score to 0 to 1
        # Use the model to make a prediction
        prediction = model.predict(X_test_manual).tolist()[0]

        # Create a response
        print("Prediction: ", prediction)
        response_data = {
            'grade': prediction,
        }
        return JsonResponse(response_data)
    
    # If it's not a POST request, return an error
    return JsonResponse({'error': 'POST request required'}, status=405)

