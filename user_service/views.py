import datetime
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer


class CategoryViewSet(ViewSet):
    """
    """

    queryset = Question.objects.all()


async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

