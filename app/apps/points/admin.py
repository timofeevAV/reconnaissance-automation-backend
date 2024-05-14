from django.contrib import admin
from .models import Point, PointPhoto, PointSample, CharacteristicValue
from django.utils.html import mark_safe


def delete_selected(self, request, queryset):
    queryset.delete()


class PointPhotoInline(admin.TabularInline):
    model = PointPhoto
    extra = 0


class PointSampleInline(admin.TabularInline):
    model = PointSample
    extra = 0


@admin.register(PointSample)
class PointSampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'sample', 'point']
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


@admin.register(CharacteristicValue)
class CharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'characteristic', 'pointSample',
                    'value']
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    inlines = [PointPhotoInline, PointSampleInline]
    list_display = ['id', 'trip', 'createdAt',
                    'latitude', 'longitude']
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


@admin.register(PointPhoto)
class PointPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'point', 'photo']
    readonly_fields = ["photo_image"]

    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width=150 height=150 />'.format(
            url=obj.photo.url,
        )
        )
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]
