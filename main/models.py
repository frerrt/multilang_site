from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = models.TextField()
    publication_date = models.DateField()

    