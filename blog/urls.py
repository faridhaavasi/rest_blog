from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('list', views.List_of_post_API.as_view(), name='list'),
    path('list_true', views.List_of_post_true_API.as_view(), name='list_true'),
    path('detail/<int:pk>', views.Detail_post_API.as_view(), name='detail'),
    path('add_post', views.Add_post_API.as_view(), name='add_post'),
    path('update_delete/<int:pk>', views.Update_Delete_post_API.as_view()),
    path('add_comment', views.Add_comment.as_view()),
]