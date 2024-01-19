from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'), # 권승훈
    path('recommend/<int:traveler_id>/',views.recommend, name='recommend'),
    path("result/<int:traveler_id>/", views.result, name='result'), # 현승엽
]