from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date   = models.DateTimeField(auto_now_add=True)

    title_en = models.CharField(max_length=100, blank=True, null=True)
    title_fr = models.CharField(max_length=100, blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    content_fr = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title