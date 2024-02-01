from django.urls import path
from . import views

app_name = 'triprecommender'

urlpatterns = [
    path('', views.survey, name='survey'),  # 권승훈
    path('recommend/', views.recommend, name='recommend'),  # 백헌하
    path('selection/', views.selection, name='selection'),  # 임지호
    path("result/", views.result, name='result'),  # 현승엽
    path("proxy_api", views.proxy_to_kakao, name="proxy_to_kakao"),  # 임지호
]