from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializer import PromptSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes= ['api/AI/test','api/AI/test/<id>']
    return Response(routes)

@api_view(['GET'])
def getPropts(request):
    all_prompts = models.Prompt.objects.all()
    prompts = PromptSerializer(all_prompts, many=True)
    return Response(prompts.data)
