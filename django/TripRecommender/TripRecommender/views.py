from django.shortcuts import render, redirect
from .models import Traveler

def survey(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        sido = request.POST.get('sido')
        travel_style = request.POST.get('travel_style')
        travel_motive = request.POST.get('travel_motive')
        travel_companions_num = request.POST.get('travel_companions_num')
        income = request.POST.get('income')

        Traveler.objects.create(
            gender=gender,
            age=age,
            sido=sido,
            travel_style=travel_style,
            travel_motive=travel_motive,
            travel_companions_num=travel_companions_num,
            income=income,
        )

        return redirect('thank_you')

    return render(request, 'TripRecommender/survey.html')

def thank_you(request):
    return render(request, 'TripRecommender/thank_you.html')



