from django.db import models

class Traveler(models.Model):
    GENDER_CHOICES = [
        ('남', '남'),
        ('여', '여'),
    ]

    AGE_CHOICES = [
        ('1', '20'),
        ('2', '30'),
        ('3', '40'),
        ('4', '50'),
        ('5', '60'),
    ]
    
    # INCOME_CHOICES = [
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', '6'),
    #     ('7', '7'),
    #     ('8', '8'),
    #     ('9', '9'),
    #     ('10', '10'),     
    # ]

    TRAVEL_MISSION = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),  
    ]

    TRAVEL_STYLE_1 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_2 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
      
    TRAVEL_STYLE_3 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_4 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_5 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_6 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_7 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_STYLE_8 = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
    
    TRAVEL_MOTIVE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    TRAVEL_NUM_CHOICES = [
        ('1', '1회'),
        ('2', '2회'),
        ('3', '3회'),
        ('4', '4회'),
        ('5', '5회 이상'),
    ]

    TRAVEL_COMPANIONS_NUM_CHOICES = [
        ('0', '0명'),
        ('1', '1명'),
        ('2', '2명'),
        ('3', '3명'),
        ('4', '4명'),
        ('5', '5명이상'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    income = models.IntegerField()
    travel_mission_priority = models.IntegerField(choices=TRAVEL_MISSION, default=0)
    travel_style_1 = models.IntegerField(choices=TRAVEL_STYLE_1)
    travel_style_2 = models.IntegerField(choices=TRAVEL_STYLE_2)
    travel_style_3 = models.IntegerField(choices=TRAVEL_STYLE_3)
    travel_style_4 = models.IntegerField(choices=TRAVEL_STYLE_4)
    travel_style_5 = models.IntegerField(choices=TRAVEL_STYLE_5)
    travel_style_6 = models.IntegerField(choices=TRAVEL_STYLE_6)
    travel_style_7 = models.IntegerField(choices=TRAVEL_STYLE_7)
    travel_style_8 = models.IntegerField(choices=TRAVEL_STYLE_8)
    travel_motive = models.IntegerField(choices=TRAVEL_MOTIVE_CHOICES)
    travel_num = models.CharField(max_length=50, choices=TRAVEL_NUM_CHOICES)
    travel_companions_num = models.CharField(max_length=20, choices=TRAVEL_COMPANIONS_NUM_CHOICES) 

    def __str__(self):
        return f"{self.get_gender_display()} - {self.get_age_display()} - {self.get_travel_style_1_display()} - {self.get_income_display()} - {self.get_travel_style_2_display()} - {self.get_travel_style_3_display()} - {self.get_travel_style_4_display()} - {self.get_travel_style_5_display()} - {self.get_travel_style_6_display()} - {self.get_travel_style_7_display()} - {self.get_travel_style_8_display()} - {self.get_travel_motive_display()} - {self.get_travel_num_display()} - {self.get_travel_companions_num_display()}"
    
    

class TouristSpot(models.Model): # 임지호
    visit_area_name = models.CharField(max_length=100)
    xcoord = models.FloatField()
    ycoord = models.FloatField()

    def __str__(self):
        return f"{self.visit_area_name - self.xcoord,self.ycoord}"