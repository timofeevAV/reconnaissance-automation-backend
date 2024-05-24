from django.db import models

class Characteristic(models.Model):
    name = models.CharField(max_length=128, unique=True)
    expression = models.CharField(max_length=255, null=True, blank=True)


class Sample(models.Model):
    name = models.CharField(max_length=128, unique=True)
    characteristics = models.ManyToManyField(
        Characteristic, through='SampleCharacteristic')


class SampleCharacteristic(models.Model):
    сharacteristic = models.ForeignKey(
        Characteristic, on_delete=models.CASCADE)
    sample = models.ForeignKey(
        Sample, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('сharacteristic', 'sample'),)