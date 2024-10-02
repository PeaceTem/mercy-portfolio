def calc_cgpa(grade_class):
    if grade_class == 'first-class':
        return 4
    elif grade_class == 'second-class upper':
        return 3
    elif grade_class == 'second-class lower':
        return 2
    elif grade_class == 'third-class':
        return 1
    else:
        return 0
    
#Low: 1, Medium: 2, High: 0

def family_income(income):
    if income == 'High':
        return 0
    elif income == 'Medium':
        return 2
    elif income == 'Low':
        return 1
    

def Learning_Disabilities(status):
    if status == 'Yes':
        return 1
    elif status == 'No':
        return 0
    


"""
curl -X POST http://localhost:8000/api/predict -H "Content-Type: application/json" -d '{"Hours_Studied": "23", "Attendance": "56", "Sleep_Hours": "7", "Previous_cgpa": "third-class", "Learning_Disabilities": "No", "Family_Income": "Medium"}'

"""