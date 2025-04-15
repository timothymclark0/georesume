from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import JobExperience, JobMedia

class JobMediaInline(admin.TabularInline):
    model = JobMedia
    extra = 1

@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')
    search_fields = ('title', 'company', 'description')
    list_filter = ('is_current',)
    inlines = [JobMediaInline]
