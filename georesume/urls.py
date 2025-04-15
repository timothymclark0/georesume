from django.urls import path
from . import views

app_name = 'georesume'

urlpatterns = [
    path('', views.resume_view, name='resume'),
    path('api/jobs/', views.job_data_json, name='job_data'),
    path('job_geojson/', views.job_geojson, name='job_geojson'),
]

