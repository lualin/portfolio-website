from django.db import models
from django.utils import timezone

# Create your models here.

# Project Model

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=250)
    stacks = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='portfolio/images/')
    img_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name_plural = ('1. Projects')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.pk}'

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        self.last_updated = timezone.localtime(timezone.now())
        super(Project, self).save(*args, **kwargs)