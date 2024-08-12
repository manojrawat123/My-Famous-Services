from django.db import models
from django.utils.text import slugify

class MyService(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='images/', null = True, blank = True)
    description = models.TextField()
    meta_description = models.TextField(blank=True, help_text="Meta description for SEO purposes")
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MyService, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
