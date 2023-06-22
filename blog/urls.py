from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('list', views.List_of_post_API.as_view(), name='list'),
]