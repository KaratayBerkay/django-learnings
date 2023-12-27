import uuid
from django.db.models import Model, UUIDField


class ModelPrimary(Model):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True

