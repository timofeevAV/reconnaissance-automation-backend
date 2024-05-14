from django.db import models
from customFields.compressed_image_field import CompressedImageField
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from blurhash import encode
from django.contrib.auth import get_user_model


def get_scheme_path(instance, filename):
    return f'images/trips/{instance.id}/scheme/{filename}'


class TripEditor(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    trip = models.ForeignKey(
        'Trip', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('trip', 'user'),)


class Trip(models.Model):
    name = models.CharField(max_length=100)
    scheme = CompressedImageField(
        upload_to=get_scheme_path, blank=True, null=True, quality=75)
    blurhash = models.CharField(
        max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)
    editors = models.ManyToManyField(
        get_user_model(), through='TripEditor', related_name='edited_trips')

    def add_editor(self, editor_user):
        TripEditor.objects.create(user=editor_user, trip=self)

    def remove_editor(self, editor_user):
        TripEditor.objects.filter(user=editor_user, trip=self).delete()

    def save(self, *args, **kwargs):
        old_instance = Trip.objects.filter(pk=self.pk).first()
        if not self.scheme:
            self.blurhash = None
            super().save(*args, **kwargs)
        elif (old_instance and self.scheme != old_instance.scheme) or (self.scheme and not old_instance):
            with self.scheme.open() as image:
                blurhash = encode(image, 4, 3)
                self.blurhash = blurhash
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updatedAt']


class TripDate(models.Model):
    day = models.DateField()
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='dates')


@receiver([post_delete, post_save], sender=TripDate)
def update_trip_updated_at(sender, instance, **kwargs):
    instance.trip.updatedAt = timezone.now()
    instance.trip.save(update_fields=['updatedAt'])