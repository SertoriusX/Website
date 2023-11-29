from django.db import models

# Create your models here.
class yugioh(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    power=models.CharField(max_length=100)
    defense=models.CharField(max_length=100)
    foto = models.URLField(blank=True,null=True)

class yugioh1(models.Model):
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    test = models.CharField(max_length=100)
    prueba = models.CharField(max_length=100)
    cards=models.ForeignKey(yugioh,on_delete=models.CASCADE)
