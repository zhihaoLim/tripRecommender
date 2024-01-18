from django.http import HttpResponse
from django.shortcuts import render
# view_test1
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# view_test2
# =======







# baik
# =======







# adfasdkfjlkdasjdlkfsjassdf
def result(request):
    return render(request, 'TripRecommender/result.html')