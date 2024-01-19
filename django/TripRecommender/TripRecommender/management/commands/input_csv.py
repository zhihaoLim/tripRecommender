import csv
from django.core.management.base import BaseCommand
from TripRecommender.models import TouristSpot

class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'VISIT_AREA_NM' in row:
                    TouristSpot.objects.create(
                        visit_area_name=row['VISIT_AREA_NM'],
                        xcoord=row['X_COORD'],
                        ycoord=row['Y_COORD'],
                    )
