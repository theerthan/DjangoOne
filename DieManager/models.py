from django.db import models
from django.db.models.functions import Cast
from django.db.models import FloatField
from datetime import date

# Create your models here.

class die(models.Model):

    class DieStatus(models.TextChoices):
        NEW = "New"
        ACTIVE = "Active"
        SUSPENDED = "Suspended"
        DECOMMISSIONED = "Decommissioned"

    Name = models.CharField(max_length=150)
    LaunchDate = models.DateField()
    ExpectedLife = models.IntegerField()
    Product = models.CharField(max_length=150)
    ActualLife = models.IntegerField(blank=True, null=True)
    DecommissionedOn = models.DateField(blank=True, null=True)
    Status = models.CharField(max_length=15, choices=DieStatus.choices, default=DieStatus.NEW)

    def __str__(self):
        return "[ " + str(self.id) + " " + self.Name + " ]"

class batch(models.Model):
    Die = models.ForeignKey(to=die, on_delete=models.PROTECT)
    RunDate = models.DateField(default=date.today())
    ExpectedUnits = models.IntegerField()
    ActualUnits = models.IntegerField()
    ErrorRate = models.DecimalField(max_digits=4, decimal_places=2,
                                    default=0.0)

    def __str__(self):
        return "[ " + str(self.RunDate) + " " + str(self.Die) + " ]"


