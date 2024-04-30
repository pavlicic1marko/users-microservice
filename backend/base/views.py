from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer, UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = ['api/products', 'api/products/<id>']
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getUserProfile(request):
    user = request.user

    serializer = UserSerializer(user, many=False)


    return Response(serializer.data)


@api_view(['GET'])
def getProductsById(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)
