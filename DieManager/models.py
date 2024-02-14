from django.db import models

# Create your models here.

class die(models.Model):
    Name = models.CharField(max_length=150)
    LaunchDate = models.DateField()
    ExpectedLife = models.IntegerField()
    Product = models.CharField(max_length=150)
    ActualLife = models.IntegerField()
    DecommisionedOn = models.DateField()

    def __str__(self):
        return Name
