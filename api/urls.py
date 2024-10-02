from django.urls import path
from .views import PredictView, my_json_view

urlpatterns = [
    path("predict", PredictView.as_view(), name="predict-home"),
    path("predict/final_grade", my_json_view, name="predict"),
]

