from .serializer import UserSerializer, JobSerializer
from user_service.models import User, Job

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request


class UserViewList(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request: Request):
        query_set = User.objects.filter(**request.data).all()
        items = {
            "count": len(query_set),
            "data": query_set.values()
        }
        return Response(items)


class UserViewGet(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def get(request: Request, uuid_ref: str):
        query_set = User.objects.get_queryset().filter(uuid_ref=uuid_ref).all()
        return Response(query_set.values()[0])


class UserViewPost(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request: Request):
        if User.objects.create(**request.data):
            return Response(request.data)
        raise Exception('User is not created')


class UserViewPut(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def put(request: Request, uuid_ref: str):
        return Response()


class UserViewDelete(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def delete(request: Request, uuid_ref: str):
        if query_set := User.objects.get_queryset().filter(uuid_ref=str(uuid_ref)):
            query_set.delete()
            return Response(status=200)
        return Response(status=404)


class JobView(GenericAPIView):

    serializer_class = JobSerializer

    def get(self, name: str):
        return Response(self.get_queryset())

    @staticmethod
    def post(request: Request):
        if User.objects.create(**request.data):
            return Response(request.data)
        raise Exception('User is not created')

    @staticmethod
    def put(request: Request):
        query_set = Job.objects.all()
        serializer = JobSerializer(query_set)
        return Response(serializer)

    @staticmethod
    def delete(request: Request):
        query_set = Job.objects.all()
        serializer = JobSerializer(query_set)
        return Response(serializer)
