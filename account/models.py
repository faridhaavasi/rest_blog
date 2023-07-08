from django.db import models

# Create your models here.
class Blacked(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username