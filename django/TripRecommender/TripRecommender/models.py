from django.db import models

class Traveler(models.Model):
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    ]

    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    travel_style = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.age}세 {self.get_gender_display()} - {self.income}원 소득 - {self.travel_style}"