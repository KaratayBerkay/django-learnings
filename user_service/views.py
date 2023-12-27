from .serializer import UserSerializer, JobSerializer
from user_service.models import User, Job

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class UserView(GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        User.objects.create(
            first_name="asd", last_name="dsas"
        )
        query_set = User.objects.all()
        print('query_set', query_set)
        # serializer = QuestionSerializer(query_set)
        print('serializer', query_set)
        return Response(query_set.data)


class JobView(GenericAPIView):
    serializer_class = JobSerializer

    def post(self, request):
        query_set = Job.objects.all()
        serializer = JobSerializer(query_set)
        return Response(serializer)
