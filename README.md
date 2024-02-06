# AI 기반 개인화 여행 추천 서비스 <JEJ U>

![logo](https://github.com/TripRecommender-HH/tripRecommender/assets/155603235/fe774a44-38c6-49ce-ba41-d58f7528060d)

## 프로젝트소개
model파일에 있는 catboost모델, random forest모델을 이용하여 개인의 성향에 따른 제주도의 여행지 추천을 한다. 그리고 추천된 여행지의 사진과 비슷한 다른 장소를 deep learning을 이용하여 추가 추천하여 이러한 여행지 정보들을 지도에 표시해주고, 여행스케줄을 만드는데 도움을 주는 웹페이즈를 만들었다.

## 개발기간
2024년 1월 9일 ~ 2024년 2월 7일

### 멤버구성
- 권승훈 : 유사 서비스 조사 및 insight 도출, 설문 서비스 제작 및 디자인, 이미지 기반 딥 러닝 모델 분석
- 백헌하 : 10가지 여행지추천을 위한 머신 러닝(Catboost) 모델 생성, INCOME 예측을 위한 RandomForest 모델 생성
- 임지호 : 프로젝트 총괄, 이미지 기반 딥 러닝 모델 연구(VGG16, RESNET50, InceptionV3, EfficientNet), 추천 서비스 페이지 제작
- 현승엽 : 여행자들의 스타일과 동기 그리고 여행자수를 베이스로 한 데이터 EDA, 이미지 기반 딥 러닝 모델 분석

### 개발환경
- bs4 : 0.0.1
- Django : 4.2.7
- numpy : 1.24.3
- pandas : 1.5.2
- Python : 3.11.5
- py-xgboost : 1.7.3
- scikit-image : 0.20.0
- scikit-learn : 1.2.2
- matplotlib : 3.8.2
- sklearn-pandas : 1.8.0
- xgboost : 2.0.3

### 핵심 ERD


## 데이터 분석
#### 자연과 도시 중에 어느 것을 선호하는 가
- 자연을 선호하는 사람들이 많다.
#### 새로운 지역과 익숙한 지역 중에 어느 곳을 선호하는 가
- 새로운 지역을 선호하는 사람들이 많다.
#### 휴양/휴식과 체험활동 중에 어떤 것을 선호하는 가
- 둘다 하고 싶은 사람들이 꽤 많았다.(굳이 비교하자면 휴양/휴식을 원하는 사람이 조금 더 많았다고 할까나..)
#### 사진촬영을 하고 싶은가 안하고 싶은가
- 사진촬영을 하고 싶은 사람들이 압도적으로 많았다.
#### 여행동기
- 주 이유가 일상적인 환경 및 역할에서의 탈출과 지루함 탈피와 쉴 수 있는 기회, 육체 피로 해결 및 정신적인 휴식을 위함이였다.
#### 여행동반자수
- 나홀로 여행하는 사람들이 제일 많았다.


## 주요기능
#### 10가지 여행지 추천을 위한 Catboost모델
- 여행자의 여행성향과 여러가지 개인정보를 통해 10개의 여행지를 추천해준다.
- CatboostRegressor를 사용하여 예측하였다.
- 성능은 Recall@10을 사용하여 약 22%이다.

#### 여행객 INCOME을 예측하기 위한 RandomForest모델
- 여행객의 수입을 직접적으로 물어볼 수 없기에 수입을 예측하는 모델을 만들었다.
- 여행객의 개인정보와 소비내역 중 상관관계가 높은 것을 찾아 RandomForest Classifier를 사용하여 예측하였다.
- 정확도은 0.7이다.

#### 여행객의 성향 및 개인정보를 얻기위한 페이지
- django와 javascript를 이용하여 여행객의 개인정보와 여행성향을 선택하도록 하였다.

#### 선택한 여행객의 성향 및 개인정보를 토대로 추천된 10가지의 여행지의 사진을 보여주는 페이지
- 앞의 페이지에서 성향과 개인정보를 얻은 것을 토대로 10가지 추천 여행지를 받아온다.
- 10가지 추천 여행지의 사진을 3장씩 보여주며 총 30장의 사진 중 5가지의 사진을 선택하도록 한다.

#### 페이지에서 선택한 5개의 사진을 토대로 Deep Learning을 진행하여 추가로 여행지 추천
- 미리 모든 사진에 대해 Efficientnet을 적용한 값을 csv파일로 저장해둔다.
- 선택된 5개의 사진과 유사한 다른 여행지를 저장해둔 csv파일을 토대로 추가로 추천 여행지에 더한다.

#### 최종적으로 추천된 여행지를 지도에 표시하고 여행계획을 도와주는 페이지
- 최종적으로 추천된 여행지를 지도에 표시한다.
- 추가로 여행일정(ex. 1박2일)을 선택하여 여행일정에 맞게 여행지를 추가하도록 만들었다.
- 지도에 여행일정으로 선택한 여행지들의 경로를 보여준다.



[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
