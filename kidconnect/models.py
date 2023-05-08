from django.db import models

# Create your models here.
class Evento(models.Model):
    name = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.name