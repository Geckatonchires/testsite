from django.db import models

# Create your models here.
class GunType(models.Model):
    GunType_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class GunDescription(models.Model):
    GunType = models.ForeignKey(GunType, on_delete=models.CASCADE)
    GunDescription_text = models.CharField(max_length=1500)