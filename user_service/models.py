from django.db.models import (
    CharField,
    CASCADE,
    ForeignKey,
    IntegerField,
    EmailField,
    DateTimeField,
)
from utils.primary_abstract import BaseMixin


class User(BaseMixin):
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


class Job(BaseMixin):
    user = ForeignKey(User, on_delete=CASCADE, null=True)
    name = CharField(max_length=200, help_text="Job name", null=False)
    job_starts = DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Jobs"

    def __str__(self):
        return str(self.uuid_ref)
