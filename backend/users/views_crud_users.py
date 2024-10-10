import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
import requests
import django.core.exceptions
from django.conf import settings



@api_view(['GET'])
def getRoutes(request):
    routes = ['api/products', 'api/products/<id>']
    return Response(routes)




@api_view(['GET'])
def comms(request):
    bearer_token = request.headers['Authorization']
    URL = "http://127.0.0.1:8001/api/routes"
    headers = {'content-type': 'application/json',
               'Authorization': bearer_token}

    r = requests.get(url=URL, headers=headers)
    data = r.json()

    return Response(data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):  #  updating user first_name and email


    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.save()  # save user to database

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def delUser(request, pk):
    username = pk
    try:
        user = User.objects.get(username=username)
        user.delete()
        return Response('user is deleted', status=200)

    except django.core.exceptions.ObjectDoesNotExist:

        return Response('user does not exist', status=status.HTTP_404_NOT_FOUND)
    except Exception as e:

        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



