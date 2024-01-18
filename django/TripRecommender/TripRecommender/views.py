from django.shortcuts import render, redirect
from .models import Traveler
from django.http import HttpResponse

def survey(request): #권승훈
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

def thank_you(request): #권승훈
    return render(request, 'TripRecommender/thank_you.html')


# adfasdkfjlkdasjdlkfsjassdf
def result(request): #현승엽
    return render(request, 'TripRecommender/result.html')