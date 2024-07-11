from django.urls import path
from . import views_jwt
from . import views_crud_users

urlpatterns = [
    path('users/login', views_jwt.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('routes', views_crud_users.getRoutes, name='routes'),
    path('users/profile', views_crud_users.getUserProfile, name='user-profile'),
    path('users/profile/update', views_crud_users.updateUserProfile, name='user-profile-update'),
    path('users', views_crud_users.getUsers, name='users'),
    path('users/register', views_jwt.registerUser, name='register'),
    path('users/images/upload', views_jwt.uploadImage, name='upload-image'),
    path('users/register-admin', views_jwt.registerAdminUser, name='register-admin'),
    path('comms', views_crud_users.comms, name='comms'),
    path('users/delete/<str:pk>', views_crud_users.delUser, name='user-delete-by-id'),

]
