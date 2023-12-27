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


class JobViewList(GenericAPIView):
    serializer_class = JobSerializer

    @staticmethod
    def post(request: Request):
        query_set = Job.objects.filter(**request.data).all()
        items = {
            "count": len(query_set),
            "data": query_set.values()
        }
        return Response(items)


class JobViewGet(GenericAPIView):
    serializer_class = JobSerializer

    @staticmethod
    def get(request: Request, uuid_ref: str):
        query_set = Job.objects.get_queryset().filter(uuid_ref=uuid_ref).all()
        return Response(query_set.values()[0])


class JobViewPost(GenericAPIView):
    serializer_class = JobSerializer

    @staticmethod
    def post(request: Request):
        if Job.objects.create(**request.data):
            return Response(request.data)
        raise Exception('User is not created')


class JobViewPut(GenericAPIView):
    serializer_class = JobSerializer

    @staticmethod
    def put(request: Request, uuid_ref: str):
        return Response()


class JobViewDelete(GenericAPIView):
    serializer_class = JobSerializer

    @staticmethod
    def delete(request: Request, uuid_ref: str):
        if query_set := Job.objects.get_queryset().filter(uuid_ref=str(uuid_ref)):
            query_set.delete()
            return Response(status=200)
        return Response(status=404)
