from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    
] + [path(page + '/',views.coming_soon, name=page) for page in ['applications']]