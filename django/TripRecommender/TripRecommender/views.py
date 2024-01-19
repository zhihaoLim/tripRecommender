from django.shortcuts import render, redirect
from .models import Traveler
from django.http import HttpResponse
from django.apps import apps
import pandas as pd


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


def recommend_places(request,traveler,model): #백헌하
    info = pd.read_csv('model/관광지 추천시스템 Testset- 여행지 정보.csv')
    try_1 = pd.DataFrame(columns=['VISIT_AREA_NM', 'SI', 'Dong_Eup', 'VISIT_AREA_TYPE_CD',
                            'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                            'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                            'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                            'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
                            'RESIDENCE_TIME_MIN_mean', 'REVISIT_YN_mean',
                            'TRAVEL_COMPANIONS_NUM_mean'])
    try_1 = info[['VISIT_AREA_NM', 'SI', 'Dong_Eup', 'VISIT_AREA_TYPE_CD',
            'RESIDENCE_TIME_MIN_mean', 'REVISIT_YN_mean',
            'TRAVEL_COMPANIONS_NUM_mean']].copy()
    try_1['TRAVEL_MISSION_PRIORITY'] = traveler.travel_mission_priority
    try_1['GENDER'] = traveler.gender
    try_1['AGE_GRP'] = traveler.age_grp
    try_1['INCOME'] = traveler.income
    try_1['TRAVEL_STYL_1'] = traveler.travel_styl_1
    try_1['TRAVEL_STYL_2'] = traveler.travel_styl_2
    try_1['TRAVEL_STYL_3'] = traveler.travel_sty1_3
    try_1['TRAVEL_STYL_4'] = traveler.travel_sty1_4
    try_1['TRAVEL_STYL_5'] = traveler.travel_sty1_5
    try_1['TRAVEL_STYL_6'] = traveler.travel_sty1_6
    try_1['TRAVEL_STYL_7'] = traveler.travel_sty1_7
    try_1['TRAVEL_STYL_8'] = traveler.travel_sty1_8
    try_1['TRAVEL_MOTIVE_1'] = traveler.travel_motive_1
    try_1['TRAVEL_NUM'] = traveler.travel_num
    try_1['TRAVEL_COMPANIONS_NUM'] = traveler.travel_companions_num

    try_1 = try_1[['VISIT_AREA_NM', 'SI', 'Dong_Eup', 'VISIT_AREA_TYPE_CD',
        'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
        'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
        'RESIDENCE_TIME_MIN_mean', 'REVISIT_YN_mean',
        'TRAVEL_COMPANIONS_NUM_mean']]
    try_1.reset_index(drop = True, inplace = True)
    try_1.drop_duplicates(['VISIT_AREA_NM'], inplace = True)

    y_pred_first_test = model.predict(try_1)
    y_pred_first_test_df = pd.DataFrame(y_pred_first_test, columns=['y_pred'])
    test_df_first_test = pd.concat([try_1, y_pred_first_test_df], axis=1)

    test_df_first_test.sort_values(by=['y_pred'], axis=0, ascending=False, inplace=True)
    top_10_recommendations = test_df_first_test.iloc[0:10,]['VISIT_AREA_NM'].tolist()
    return top_10_recommendations


def recommend(request, traveler_id): #백헌하
    model = apps.get_app_config('TripRecommender').model
    traveler = Traveler.objects.get(id=traveler_id)
    recommended_places = recommend_places(traveler,model)
    return redirect('result',traveler_id=traveler.id, recommended_places = recommended_places)



