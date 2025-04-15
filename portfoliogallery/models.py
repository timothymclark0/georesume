from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    ARTIFACT_CHOICES = (
        ('image', 'Image Gallery'),
        ('video', 'Video'),
        ('pdf', 'PDF Document'),
        ('github', 'GitHub Repository'),
        ('website', 'Live Website'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name='projects')
    skills = models.ManyToManyField(Skill, related_name='projects')
    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='projects/featured/')
    date_created = models.DateField()
    date_completed = models.DateField(null=True, blank=True)
    primary_artifact_type = models.CharField(max_length=20, choices=ARTIFACT_CHOICES)
    github_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_completed', '-date_created']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"

class ProjectPDF(models.Model):
    project = models.ForeignKey(Project, related_name='pdfs', on_delete=models.CASCADE)
    file = models.FileField(upload_to='projects/pdfs/')
    title = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project PDF"
        verbose_name_plural = "Project PDFs"
    
    def __str__(self):
        return f"{self.project.title} - {self.title}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, related_name='videos', on_delete=models.CASCADE)
    url = models.URLField(help_text="YouTube or Vimeo URL")
    title = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - {self.title}"