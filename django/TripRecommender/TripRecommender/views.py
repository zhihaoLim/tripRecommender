from django.shortcuts import render, redirect
from .models import Traveler

def survey(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        income = request.POST.get('income')
        travel_style = request.POST.get('travel_style')

        Traveler.objects.create(
            age=age,
            gender=gender,
            income=income,
            travel_style=travel_style
        )

        return redirect('thank_you')

    return render(request, 'TripRecommender/survey.html')

def thank_you(request):
    return render(request, 'TripRecommender/thank_you.html')



