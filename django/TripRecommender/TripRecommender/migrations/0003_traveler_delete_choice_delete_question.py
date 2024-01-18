# Generated by Django 4.2.7 on 2024-01-18 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "TripRecommender",
            "0002_choice_question_delete_answer_delete_survey_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Traveler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "남성"), ("F", "여성"), ("O", "기타")], max_length=1
                    ),
                ),
                ("income", models.DecimalField(decimal_places=2, max_digits=10)),
                ("travel_style", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Choice",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
