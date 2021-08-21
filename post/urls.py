from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.thought_create_view, name='posts')
]
