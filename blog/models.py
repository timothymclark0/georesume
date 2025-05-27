from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=25)

    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    body = models.TextField()
    slug = models.SlugField(blank=True)
    date_posted = models.DateTimeField(default = now)
    tags = models.ManyToManyField(Tag, related_name='post_tag', blank=True)
    featured_image = models.ImageField(upload_to='static/blog/posts/featured/', blank=True,null=True)
    featured_post = models.BooleanField(default = False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['-date_posted']


