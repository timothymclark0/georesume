from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<str:slug>', view_post, name = 'view_post'),
    path('posts', post_list, name = 'post_list'),
]