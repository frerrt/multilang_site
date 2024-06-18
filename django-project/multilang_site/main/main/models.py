# main/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Renommé contents à content pour respecter la norme Django
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
