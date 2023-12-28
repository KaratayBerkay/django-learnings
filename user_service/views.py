from .serializer import UserSerializer, JobSerializer
from user_service.models import User, Job

from django.db.models import Q

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from typing import Optional

filter_expression = Q(firstname__startswith='asdasd')


class StandardJsonResponse:

    def __init__(self, data=None, message: str = "", status_code: int = 500):
        self.data: Optional = data
        self.count: int = 0
        self.message: Optional[str] = message
        if self.data:
            if isinstance(self.data, list):
                self.count = len(self.data)
            elif isinstance(self.data, dict):
                self.count = 1
            else:
                self.count = self.data.count()
            [item.pop('id') for item in self.data or []]    # Remove ids
            self.response: Response = Response(
                data={"count": self.count, "data": self.data or []}, status=200
            )
        if self.message:
            self.response: Response = Response(
                data={"count": self.count, "message": message, "data": self.data or []}, status=status_code
            )


class UserViewBase(GenericAPIView):
    serializer_class = UserSerializer
    object = User.objects.get_queryset()


class UserViewList(UserViewBase):

    def post(self, request: Request):

        if filter_dict := getattr(request, 'data'):
            if query_set := self.object.filter(**filter_dict).all():
                return StandardJsonResponse(data=query_set.values()).response
        else:
            if query_set := self.object.filter().all():
                return StandardJsonResponse(data=query_set.values()).response
        return StandardJsonResponse(
            message="No User found @Database", status_code=status.HTTP_404_NOT_FOUND
        ).response


class UserViewGet(UserViewBase):

    @staticmethod
    def get(request: Request, uuid_ref: str):
        if not len(uuid_ref) == 36:
            return StandardJsonResponse(
                message=f"Given uuid is not valid", status_code=status.HTTP_400_BAD_REQUEST
            ).response
        if query_set := User.objects.filter(uuid_ref=uuid_ref).all():
            return StandardJsonResponse(data=query_set.values()[0]).response
        return StandardJsonResponse(message="No User found @Database", status_code=status.HTTP_404_NOT_FOUND).response


class UserViewPost(UserViewBase):

    def post(self, request: Request):
        add_data = getattr(request, 'data')
        if not add_data:
            return StandardJsonResponse(
                message=f"No data found in request", status_code=status.HTTP_400_BAD_REQUEST
            ).response
        if self.serializer_class(data=add_data).is_valid():
            self.object.get_or_create(**add_data)
            return StandardJsonResponse(data=add_data).response
        return StandardJsonResponse(
            message=f"User add request is invalid", status_code=status.HTTP_400_BAD_REQUEST
        ).response


class UserViewPut(UserViewBase):

    @staticmethod
    def put(request: Request, uuid_ref: str):
        if not len(uuid_ref) == 36:
            return StandardJsonResponse(
                message=f"Given uuid is not valid", status_code=status.HTTP_400_BAD_REQUEST
            ).response
        return Response()


class UserViewDelete(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def delete(request: Request, uuid_ref: str):
        if not len(uuid_ref) == 36:
            return StandardJsonResponse(
                message=f"Given uuid is not valid", status_code=status.HTTP_400_BAD_REQUEST
            ).response
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
