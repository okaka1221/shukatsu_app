from django.urls import path
from . import views

urlpatterns = [
    path('text-analysis/', views.TextAnalysisResult.as_view())
]