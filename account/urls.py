from django.urls import path
from rest_framework.authtoken import views as auth_view
from . import views
urlpatterns = [
    path('register', views.Register.as_view()),
    path('login', auth_view.obtain_auth_token),
    path('check', views.Chek_user.as_view()),
]