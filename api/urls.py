from django.urls import path
from .views import DataExtractor

urlpatterns = [
    path('v1/', DataExtractor.as_view()),

]
