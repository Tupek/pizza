from django.db import models


class Index(models.Model):
    subheading = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/index/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
