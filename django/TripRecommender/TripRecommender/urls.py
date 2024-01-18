from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'), # 권승훈
    path('thank_you/', views.thank_you, name='thank_you'), # 권승훈
    path("result/", views.result, name='result'), # 현승엽
]