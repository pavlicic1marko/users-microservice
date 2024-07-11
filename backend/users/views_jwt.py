from django.db.utils import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializerWithToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .constants.error_messages import USER_WITH_EMAIL_EXISTS, SERVER_ERROR


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
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except IntegrityError:
        message = {'detail': USER_WITH_EMAIL_EXISTS}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    except:
        message = {'detail': SERVER_ERROR}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def registerAdminUser(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password']),
            is_staff = 1,
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except IntegrityError:
        message = {'detail': USER_WITH_EMAIL_EXISTS}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    except:
        message = {'detail': SERVER_ERROR}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def uploadImage(request):
    data = request.data

    first_name = data['image']
    type_name =type(first_name)


    return Response(str(type_name))