from django.apps import AppConfig
import joblib
import os

from django.apps import AppConfig
import joblib
import os

class TripRecommenderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TripRecommender"
    verbose_name = 'TripRecommender_App'

    catboost_model_path = os.path.join(os.path.dirname(__file__), 'catboost_model.pkl')
    rf_model_path = os.path.join(os.path.dirname(__file__), 'rf_model_for_income.pkl')
    catboost_model = None
    rf_model = None

    def ready(self):
        if not self.catboost_model:
            self.catboost_model = joblib.load(self.catboost_model_path)
        if not self.rf_model:
            self.rf_model = joblib.load(self.rf_model_path)
