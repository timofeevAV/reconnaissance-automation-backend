from django.contrib import admin
from .models import Trip, TripDate, TripEditor
from apps.points.models import Point
from django import forms
from django.utils.html import mark_safe


def delete_selected(self, request, queryset):
    queryset.delete()


class TripEditorInline(admin.TabularInline):
    model = TripEditor
    extra = 0


class PointInline(admin.TabularInline):
    model = Point
    extra = 0


class TripDateInline(admin.TabularInline):
    model = TripDate
    extra = 0


@admin.register(TripEditor)
class TripEditorAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip', 'user')
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


@admin.register(TripDate)
class TripDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip', 'day')
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


class TripAdminForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class TripAdmin(admin.ModelAdmin):
    inlines = [PointInline, TripDateInline, TripEditorInline]
    list_display = ['id', 'name', 'updatedAt', 'display_editors']
    form = TripAdminForm
    search_fields = ['name']
    readonly_fields = ["scheme_image"]

    def scheme_image(self, obj):
        return mark_safe('<img src="{url}" width=150 height=150 />'.format(
            url=obj.scheme.url,
        )
        )

    def display_editors(self, obj):
        return ", ".join([editor.firstName for editor in obj.editors.all()])

    display_editors.short_description = "Editors"
    delete_selected.short_description = 'Удалить'
    actions = [delete_selected]


admin.site.register(Trip, TripAdmin)
