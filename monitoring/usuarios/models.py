from django.db import models

class Usuario (models.Model):
    nombre=models.CharField(max_length=50)
    profesion=models.CharField(max_length=50)
    eps=models.CharField(max_length=50)


    def __str__(self):
        return '%s %s' % (self.nombre, self.profesion)