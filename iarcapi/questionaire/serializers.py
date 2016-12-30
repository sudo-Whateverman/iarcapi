from rest_framework import serializers
from questionaire.models import examQA


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = examQA
        fields = ('id', 'Question', 'CorrectAnswer', 'AdditionalAnswer1', 'AdditionalAnswer2', 'AdditionalAnswer3')

