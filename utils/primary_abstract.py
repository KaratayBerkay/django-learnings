import uuid
from django.db.models import Model, UUIDField


class ModelPrimary(Model):
    uuid_ref = UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, auto_created=True)

    class Meta:
        abstract = True
