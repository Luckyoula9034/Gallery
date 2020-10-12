from django.db import models

# Create your models here.
from django.db import models

class Editor(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)


    def __str__(self):
        return self.name