from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("survey/", include("TripRecommender.urls")),
    path("admin/", admin.site.urls),
]