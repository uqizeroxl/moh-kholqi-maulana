from django.db import models

# Create your models here.
class Biodata(models.Model):
    nama = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    Npm = models.IntegerField()
    