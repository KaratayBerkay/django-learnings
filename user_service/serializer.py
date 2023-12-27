from user_service.models import User, Job
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField, EmailField, IntegerField
from .models import User, Job


class UserSerializer(ModelSerializer):

    first_name = CharField(source="first_name", required=True)
    last_name = CharField(source="last_name", required=True)
    age = IntegerField(source="age")
    location = CharField(source="location")
    email = EmailField(source="email")

    class Meta:
        model = User
        fields = '__all__'


class JobSerializer(ModelSerializer):
    user_id = IntegerField(source='user_id')
    name = CharField(source="name")
    description = CharField(source="description")

    class Meta:
        model = Job
        fields = '__all__'
