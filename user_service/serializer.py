from user_service.models import User, Job
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField, EmailField, IntegerField, DateTimeField


class UserSerializer(ModelSerializer):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    age = IntegerField(required=True)
    location = CharField()
    email = EmailField()

    class Meta:
        model = User
        fields = "__all__"


class JobSerializer(ModelSerializer):

    name = CharField(min_length=20, max_length=200)
    job_starts = DateTimeField()

    class Meta:
        model = Job
        fields = ["name", "job_starts"]
