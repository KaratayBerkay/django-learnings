from django.db.backends.postgresql.base import DatabaseWrapper as DatabaseWrapperC
from django.db.backends.postgresql.features import DatabaseFeatures as DatabaseFeaturesC


class DatabaseFeatures(DatabaseFeaturesC):
    def allows_group_by_selected_pks_on_model(self, model):
        return True


class DatabaseWrapper(DatabaseWrapperC):
    features_class = DatabaseFeatures
