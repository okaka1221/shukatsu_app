from django.urls import path
from api.entrysheet import views

urlpatterns = [
    path('text-analysis/', views.TextAnalysisResult.as_view())
]