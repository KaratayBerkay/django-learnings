import datetime
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer


@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass


async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

