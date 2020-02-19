from django.urls import path
from api.entrysheet import views

urlpatterns = [
    path('entrysheet/', views.EntrySheetResult.as_view(), name='entrysheet')
]