from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    qr = models.CharField(max_length=999, null=False, blank=False)
    photo = models.ImageField(upload_to='photos', null=False, blank=False)
    number = models.IntegerField(unique=True, primary_key=True, null=False, blank=False,
                                 validators=[MaxValueValidator(999), MinValueValidator(1)])
