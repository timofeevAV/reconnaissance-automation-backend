from django.db import models
from customFields.compressed_image_field import CompressedImageField
from apps.trips.models import Trip
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from blurhash import encode
from apps.samples.models import Sample, Characteristic


def get_photo_point_path(instance, filename):
    return f'images/trips/{instance.point.trip.id}/points/{instance.point.id}/{filename}'


class Point(models.Model):
    latitude = models.DecimalField(
        max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    samples = models.ManyToManyField(
        Sample, through='PointSample')
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='points')

    class Meta:
        ordering = ['createdAt']


class PointPhoto(models.Model):
    photo = CompressedImageField(
        upload_to=get_photo_point_path, blank=True, null=True, quality=75)
    point = models.ForeignKey(
        Point, on_delete=models.CASCADE, related_name='photos')
    blurhash = models.CharField(
        max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.photo:
            self.blurhash = None
            super().save(*args, **kwargs)
            return
        old_instance = Trip.objects.filter(pk=self.pk).first()
        if (old_instance and self.photo != old_instance.scheme) or (self.photo and not old_instance):
            with self.photo.open() as image:
                blurhash = encode(image, 4, 3)
                self.blurhash = blurhash
                super().save(*args, **kwargs)


class PointSample(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)


class CharacteristicValue(models.Model):
    characteristic = models.ForeignKey(
        Characteristic, on_delete=models.CASCADE)
    pointSample = models.ForeignKey(PointSample, on_delete=models.CASCADE)
    value = models.CharField(max_length=128)


@receiver([post_delete, post_save], sender=PointSample)
def update_trip_updated_at(sender, instance, **kwargs):
    instance.point.trip.updatedAt = timezone.now()
    instance.point.trip.save(update_fields=['updatedAt'])


@receiver([post_delete, post_save], sender=Point)
def update_trip_updated_at(sender, instance, **kwargs):
    instance.trip.updatedAt = timezone.now()
    instance.trip.save(update_fields=['updatedAt'])


@receiver([post_delete, post_save], sender=PointPhoto)
def update_trip_updated_at(sender, instance, **kwargs):
    instance.point.trip.updatedAt = timezone.now()
    instance.point.trip.save(update_fields=['updatedAt'])