
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from questionaire.models import examQA
from questionaire.serializers import QuestionSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def questionview(ModelViewSet):
    queryset = examQA.objects.all()
    serializer_class = QuestionSerializer

@csrf_exempt
def questionview_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        exam_questions = examQA.objects.all()
        serializer = QuestionSerializer(exam_questions, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def questionview_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        exam_question = examQA.objects.get(pk=pk)
    except examQA.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(exam_question)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(exam_question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        exam_question.delete()
        return HttpResponse(status=204)