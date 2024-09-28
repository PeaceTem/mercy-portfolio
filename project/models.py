from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Project(models.Model):
    name = models.CharField(verbose_name="project name", max_length=100,)
    description = models.TextField(max_length=1000,)
    image = models.ImageField(upload_to="projects/")
    link = models.URLField(verbose_name="web link", default="#")

    class Meta:
        verbose_name="My Project"
        verbose_name_plural="My Projects"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Add custom save logic here (if needed)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def clean(self):
        # Custom validation logic
        if not self.name:
            raise ValidationError('The project name cannot be empty.')
        if len(self.description) < 10:
            raise ValidationError('The project description should be at least 10 characters long.')

    def __unicode__(self):
        return self.name
    
