from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

  
    def __str__(self):
        return self.title