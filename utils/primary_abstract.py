import uuid
from django.db.models import Model, UUIDField
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
    CreationDateTimeField,
)
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
)


class ExtensionMixin(ActivatorModel, TitleDescriptionModel, TimeStampedModel, CreationDateTimeField):
    class Meta:
        abstract = True


class CrudMixin(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    class Meta:
        abstract = True


class BaseMixin(ExtensionMixin, Model):
    uuid_ref = UUIDField(default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        abstract = True

