# survey_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_view, name='survey-form'),
    path('kiitos/', views.survey_thanks_view, name='survey-thanks'),
]


