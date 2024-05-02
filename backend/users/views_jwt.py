from django.db.utils import IntegrityError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializerWithToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.


@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = User.objects.create_user(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except IntegrityError:
        message = {'detail': 'user with this eamil exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    except:
        message = {'detail': 'internal server error'}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
