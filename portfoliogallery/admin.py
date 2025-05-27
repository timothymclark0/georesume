from django.contrib import admin
from .models import *

class InlineSkill(admin.TabularInline):
    model = Skill
    extra = 1

class InlineCategory(admin.TabularInline):
    model = Category
    
class InlineProjectImage(admin.TabularInline):
    model = ProjectImage 

class InlineProjectPDF(admin.TabularInline):
    model = ProjectPDF 

class InlineProjectVideo(admin.TabularInline):
    model = ProjectVideo

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'short_description','created_at',
                    'primary_artifact_type', 'date_completed')
    search_fields = ('title','skills','categories')
    inlines = [InlineProjectImage,InlineProjectPDF,InlineProjectVideo]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    search_fields = ('name',)
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)