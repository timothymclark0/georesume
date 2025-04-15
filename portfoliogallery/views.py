from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Category

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True).order_by('-date_completed')[:3]
        context['categories'] = Category.objects.all()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get next and previous projects
        project = self.object
        all_projects = list(Project.objects.all())
        current_index = all_projects.index(project)
        
        if current_index > 0:
            context['previous_project'] = all_projects[current_index - 1]
        if current_index < len(all_projects) - 1:
            context['next_project'] = all_projects[current_index + 1]
            
        return context

class CategoryProjectsView(ListView):
    template_name = 'portfolio/category_projects.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Project.objects.filter(categories=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['featured_projects'] = self.get_queryset().filter(featured=True)[:2]
        return context