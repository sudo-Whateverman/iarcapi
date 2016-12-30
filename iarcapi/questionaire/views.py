
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from questionaire.models import examQA
from questionaire.serializers import QuestionSerializer


def questionview(ModelViewSet):
    queryset = examQA.objects.all()
    serializer_class = QuestionSerializer

