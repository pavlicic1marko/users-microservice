import jwt
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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

 #    order = Order.objects.get(_id=pk)
@api_view(['GET'])
def getPromptsByUserId(request, pk):
    all_prompts = models.Prompt.objects.filter(user_id=pk)
    prompts = PromptSerializer(all_prompts, many=True)
    return Response(prompts.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def answerPrompt(request):
    data = request.data
    prompt = data['prompt']

    bearer_token = request.headers['Authorization'].split()[1]
    payload = jwt.decode(jwt=bearer_token, key=settings.SECRET_KEY, algorithms=['HS256'])
    use_id = payload['user_id']


    API_call = 'test anwer'

    models.Prompt.objects.create(
        user_id=use_id,
        prompt=prompt,
        answer='answer',
    )
    return Response(API_call)