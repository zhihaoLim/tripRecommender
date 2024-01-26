from django.shortcuts import render, redirect
from .models import Traveler, TouristSpot
from django.http import HttpResponse
from django.apps import apps
import pandas as pd
import requests
import json
from django.http import JsonResponse

#catboost_model = apps.get_app_config('TripRecommender').catboost_model
#random_forest_model = apps.get_app_config('TripRecommender').rf_model

def conv_income(age,payment):
    random_forest_model = apps.get_app_config('TripRecommender').rf_model
    input_var = pd.DataFrame(columns=['AGE_GRP','ALL_PAYMENT_AMT_WON_mean_sep'])
    input_var['AGE_GRP'] = [age]
    input_var['ALL_PAYMENT_AMT_WON_mean_sep'] = [payment]


    return random_forest_model.predict(input_var)

def survey(request): #권승훈
    if request.method == 'POST':
        print('travel_motive:',request.POST.get('travel_motive'))
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        payment = request.POST.get('payment')
        travel_mission = request.POST.get('travel_mission')
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

        traveler = Traveler.objects.create(
            gender=gender,
            age=age,
            income=conv_income(age,payment),
            travel_mission_priority=travel_mission,
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
        
        request.session['traveler_id'] = traveler.id
        return redirect('triprecommender:recommend')

    return render(request, 'TripRecommender/survey.html')


def recommend_places(traveler,model): #백헌하
    info = pd.read_csv('관광지 추천시스템 Testset- 여행지 정보.csv')
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
    try_1['AGE_GRP'] = traveler.age
    try_1['INCOME'] = traveler.income
    try_1['TRAVEL_STYL_1'] = traveler.travel_style_1
    try_1['TRAVEL_STYL_2'] = traveler.travel_style_2
    try_1['TRAVEL_STYL_3'] = traveler.travel_style_3
    try_1['TRAVEL_STYL_4'] = traveler.travel_style_4
    try_1['TRAVEL_STYL_5'] = traveler.travel_style_5
    try_1['TRAVEL_STYL_6'] = traveler.travel_style_6
    try_1['TRAVEL_STYL_7'] = traveler.travel_style_7
    try_1['TRAVEL_STYL_8'] = traveler.travel_style_8
    try_1['TRAVEL_MOTIVE_1'] = traveler.travel_motive
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


def recommend(request): #백헌하
    traveler_id = request.session.get('traveler_id')
    catboost_model = apps.get_app_config('TripRecommender').catboost_model
    traveler = Traveler.objects.get(id=traveler_id)
    recommended_places = recommend_places(traveler,catboost_model)
    
    # 추천된 장소 목록을 세션에 저장
    request.session['recommended_places'] = recommended_places

    return redirect('triprecommender:result')

def result(request):
    traveler_id = request.session.get('traveler_id')
    traveler = Traveler.objects.get(id=traveler_id)

    # 세션에서 추천된 장소 목록 가져오기
    recommended_places = request.session.get('recommended_places', [])
    print(recommended_places)

    # TouristSpot 객체들 조회
    tourist_spots = TouristSpot.objects.filter(visit_area_name__in=recommended_places)
    
    

    if request.method == 'POST':
        # Traveler 인스턴스 삭제 및 survey 페이지로 리디렉션
        traveler.delete()
        return redirect('triprecommender:survey')
    
    # 추천된 장소와 Traveler 객체 전달
    context = {
        'places': tourist_spots,
        'traveler': traveler
    }

    return render(request, 'TripRecommender/result.html', context)




def proxy_to_kakao(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            external_url = 'https://apis-navi.kakaomobility.com/v1/waypoints/directions'
            headers = {
                'Authorization': 'KakaoAK 27614dd93f27629969a759981d623f4b',
                'Content-Type': 'application/json'
            }

            response = requests.post(external_url, headers=headers, json=data)
            response.raise_for_status()
            print(response.json().get("routes")[0].get("result_msg"))
            return JsonResponse(response.json())
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)