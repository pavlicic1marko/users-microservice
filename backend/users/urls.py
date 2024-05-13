from django.urls import path
from . import views_jwt
from . import views_crud_users

urlpatterns = [
    path('users/login', views_jwt.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('routes', views_crud_users.getRoutes, name='routes'),
    path('products', views_crud_users.getProducts, name='products'),
    path('products/<str:pk>', views_crud_users.getProductsById, name='products'),
    path('users/profile', views_crud_users.getUserProfile, name='user-profile'),
    path('users/profile/update', views_crud_users.updateUserProfile, name='user-profile-update'),
    path('users', views_crud_users.getUsers, name='users'),
    path('users/register', views_jwt.registerUser, name='register'),
    path('comms', views_crud_users.comms, name='comms'),
    path('users/delete/<str:pk>', views_crud_users.delUser, name='user-delete-by-id'),

]
