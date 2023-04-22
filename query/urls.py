from django.urls import path
from . import views

urlpatterns = [    
    path('getAllPredictionsByEmail/',views.getAllResultsByEmail),
    path('getAllResultsFileByEmail/',views.getAllResultsFileByEmail),
    path('getCurrentResultPrediction/',views.getCurrentResultPrediction),
    path('getCurrentResultPredictionFile/',views.getCurrentResultPredictionFile),
]