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

 #    order = Order.objects.get(_id=pk)
@api_view(['GET'])
def getPromptsById(request, pk):
    all_prompts = models.Prompt.objects.filter(user_id=pk)
    prompts = PromptSerializer(all_prompts, many=True)
    return Response(prompts.data)

@api_view(['GET'])
def answerPrompt(request):
    data = request.data
    prompt = data['prompt']

    models.Prompt.objects.create(
        user_id=3,
        prompt=prompt,
        answer='answer',
    )
    # TODO  get user id from token, crete random text genrator or API call

    return Response('test')