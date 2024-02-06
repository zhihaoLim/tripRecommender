import csv
from django.core.management.base import BaseCommand
from TripRecommender.models import TouristSpot, SpotImage

class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='cp949') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # TouristSpot 데이터 처리
                if 'VISIT_AREA_NM' in row:
                    TouristSpot.objects.create(
                        visit_area_name=row['VISIT_AREA_NM'],
                        xcoord=row.get('X_COORD', 0),
                        ycoord=row.get('Y_COORD', 0),
                        main_image=row.get('PHOTO_FILE_NM', None)
                    )

                # SpotImage 데이터 처리
                if 'Image' in row:
                    # 관련 TouristSpot 객체 찾기
                    tourist_spot = TouristSpot.objects.filter(visit_area_name=row.get('Place')).first()
                    if tourist_spot:
                        print('tourist_spot 있음')
                        SpotImage.objects.create(
                            image=row['Image'],
                            tourist_spot=tourist_spot,
                            rcmd_image=row['Recommended Image'],
                            similarity=float(row.get('Similarity', 0.0))
                        )