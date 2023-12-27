from django.db.models import Model, CharField, CASCADE, ForeignKey, IntegerField, EmailField
from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleDescriptionModel


class User(ActivatorModel, TimeStampedModel, TitleDescriptionModel, Model):

    first_name = CharField(max_length=200, help_text="User name", blank=False)
    last_name = CharField(max_length=200, help_text="User lastname", blank=False)
    age = IntegerField(blank=False)
    location = CharField(blank=True)
    email = EmailField(verbose_name="Email", blank=True)

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "Users"

    def __str__(self):
        return self.pk


class Job(TimeStampedModel, Model):

    user_id = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=200, help_text="Job name", blank=False)
    description = CharField(max_length=350, help_text="Job description", blank=True)

    class Meta:
        ordering = ["user_id"]
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.user_id



