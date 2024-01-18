from django.db import models

class Traveler(models.Model):
    GENDER_CHOICES = [
        ('Male', '남성'),
        ('Female', '여성'),
    ]

    AGE_CHOICES = [
        ('10s', '10대'),
        ('20s', '20대'),
        ('30s', '30대'),
        ('40s', '40대'),
        ('50s', '50대 이상'),
    ]

    SIDO_CHOICES = [
        ('Seoul', '서울'),
        ('Busan', '부산'),
        ('Incheon', '인천'),
        # 다른 시/도 추가
    ]

    TRAVEL_STYLE_CHOICES = [
        ('Adventure', '모험'),
        ('Relaxation', '휴식'),
        ('Cultural', '문화체험'),
        ('City', '도시 여행'),
        # 다른 여행 스타일 추가
    ]

    TRAVEL_MOTIVE_CHOICES = [
        ('Leisure', '휴식'),
        ('Exploration', '탐험'),
        ('Cultural_experience', '문화체험'),
        # 다른 여행 동기 추가
    ]

    TRAVEL_COMPANIONS_NUM_CHOICES = [
        ('Alone', '혼자'),
        ('With_family', '가족과'),
        ('With_friends', '친구와'),
        ('Group', '단체'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=10, choices=AGE_CHOICES)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    sido = models.CharField(max_length=20, choices=SIDO_CHOICES)
    travel_style = models.CharField(max_length=20, choices=TRAVEL_STYLE_CHOICES)
    travel_motive = models.CharField(max_length=50, choices=TRAVEL_MOTIVE_CHOICES)
    travel_companions_num = models.CharField(max_length=20, choices=TRAVEL_COMPANIONS_NUM_CHOICES) 

    def __str__(self):
        return f"{self.get_gender_display()} - {self.get_age_grp_display()} - {self.get_sido_display()} - {self.get_travel_style_display()} - {self.get_travel_motive_display()} - {self.get_travel_companions_num_display()}"