from django.shortcuts import render, redirect
from .models import Traveler

def survey(request): #권승훈
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        income = request.POST.get('income')
        travel_style_1 = request.POST.get('travel_style_1')
        travel_style_2 = request.POST.get('travel_style_2')
        travel_style_3 = request.POST.get('travel_style_3')
        travel_style_4 = request.POST.get('travel_style_4')
        travel_style_5 = request.POST.get('travel_style_5')
        travel_style_6 = request.POST.get('travel_style_6')
        travel_style_7 = request.POST.get('travel_style_7')
        travel_style_8 = request.POST.get('travel_style_8')
        travel_motive = request.POST.get('travel_motive')
        travel_num = request.POST.get('travel_num')
        travel_companions_num = request.POST.get('travel_companions_num')

        Traveler.objects.create(
            gender=gender,
            age=age,
            income=income,
            travel_style_1=travel_style_1,
            travel_style_2=travel_style_2,
            travel_style_3=travel_style_3,
            travel_style_4=travel_style_4,
            travel_style_5=travel_style_5,
            travel_style_6=travel_style_6,
            travel_style_7=travel_style_7,
            travel_style_8=travel_style_8,
            travel_motive=travel_motive,
            travel_num=travel_num,
            travel_companions_num=travel_companions_num,
        )

        return redirect('thank_you')

    return render(request, 'TripRecommender/survey.html')

def thank_you(request): #권승훈
    return render(request, 'TripRecommender/thank_you.html')


# adfasdkfjlkdasjdlkfsjassdf
def result(request): #현승엽
    return render(request, 'TripRecommender/result.html')