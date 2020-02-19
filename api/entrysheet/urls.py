from django.urls import path
from api.entrysheet import views

urlpatterns = [
    path('entrysheet/', views.TextAnalysisResult.as_view())
]