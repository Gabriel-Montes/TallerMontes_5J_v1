from django.db import models

# Create your models here.
class Alumno(models.Model):
	APaterno=models.CharField(verbose_name='Apaterno',max_length=50)
    