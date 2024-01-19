from django.apps import AppConfig
import joblib
import os


class TriprecommenderConfig(AppConfig): #백헌하
    default_auto_field = "django.db.models.BigAutoField"
    name = "TripRecommender"
    verbose_name='TripRecommender_App'

    model_path = os.path.join(os.path.dirname(__file__),'model/catboost_model.pkl')
    model = None
    
    def ready(self):
        if not self.model:
            self.model = joblib.load(self.model_path)





