from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'),
    path('thank_you/', views.thank_you, name='thank_you'),
]

