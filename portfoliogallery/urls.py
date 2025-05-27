from django.urls import path
from . import views

app_name = 'portfoliogallery'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('project/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('category/<slug:slug>/', views.CategoryProjectsView.as_view(), name='category_projects'),
]