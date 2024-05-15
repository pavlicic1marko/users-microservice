from django.urls import path
from . import views

urlpatterns = [
    path('ai/test', views.getRoutes, name='routes'),
    path('ai/prompts', views.getPropts, name='prompts'),
    path('ai/prompts/<str:pk>', views.getPromptsByUserId, name='prompts-by-user-id'),
    path('ai/answer', views.answerPrompt, name='prompts'),

]