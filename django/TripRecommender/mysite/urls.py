from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("TripRecommender/", include("TripRecommender.urls")),
    path("admin/", admin.site.urls),
]