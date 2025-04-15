from django.db import models

class JobExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    
    # Location information for the map
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)  # Two-letter state code
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    # Optional fields
    skills = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    
    # For ordering on the page
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class JobMedia(models.Model):
    job = models.ForeignKey(JobExperience, related_name='media', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='job_media/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Job Media'
    
    def __str__(self):
        return self.title