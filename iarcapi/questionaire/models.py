from django.db import models

# Create your models here.
class examQA(models.Model):
    Question = models.CharField(max_length=255)
    CorrectAnswer = models.CharField(max_length=255)
    AdditionalAnswer1 =  models.CharField(max_length=255)
    AdditionalAnswer2 = models.CharField(max_length=255)
    AdditionalAnswer3 = models.CharField(max_length=255)