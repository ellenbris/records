from django.db import models

# Create your models here.

# Takes only one field 
class Records(models.Model):
    title = models.CharField(max_length = 1000)

    def __str__(self): 
        return self.title