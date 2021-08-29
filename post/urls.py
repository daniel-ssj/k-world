from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post/', views.thought_create_view, name="create_thought"),
    path('thought/<int:id>', views.thought_detail_view, name="thought_detail"),
    path('delete/<int:id>', views.thought_delete_view, name="delete_thought"),
    path('create_comment/<int:id>', views.comment_create_view, name="create_comment")
]
