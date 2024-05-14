from django.contrib import admin
from .models import Characteristic, Sample, SampleCharacteristic


class SampleCharacteristicInline(admin.TabularInline):
    model = SampleCharacteristic
    extra = 1


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['name', 'expression']
    search_fields = ['name', 'expression']


class SampleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [SampleCharacteristicInline]


class SampleCharacteristicAdmin(admin.ModelAdmin):
    list_display = ['сharacteristic', 'sample']
    search_fields = ['сharacteristic__name', 'sample__name']


admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(SampleCharacteristic, SampleCharacteristicAdmin)
