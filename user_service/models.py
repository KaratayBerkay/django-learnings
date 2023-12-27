from django.db.models import (
    Model,
    CharField,
    DO_NOTHING,
    ForeignKey,
    IntegerField,
    EmailField,
    DateTimeField,
)
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)
from utils.primary_abstract import ModelPrimary


class User(ModelPrimary, ActivatorModel, TimeStampedModel, TitleDescriptionModel, Model):
    first_name = CharField(max_length=200, help_text="User name", null=False)
    last_name = CharField(max_length=200, help_text="User lastname", null=False)
    age = IntegerField()
    location = CharField(null=True)
    email = EmailField(null=True, verbose_name="Email")

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.uuid_ref)


class Job(ModelPrimary, TimeStampedModel, Model):
    user = ForeignKey(User, on_delete=DO_NOTHING, null=True)
    name = CharField(max_length=200, help_text="Job name", null=False)
    description = CharField(max_length=350, help_text="Job description", null=True)
    job_starts = DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.uuid_ref
