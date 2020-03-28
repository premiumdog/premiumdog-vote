from django.contrib import admin
from . models import Gallery
from django.utils.html import format_html


# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('img',)}
    list_display = ('name', 'admin_image')

    def admin_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.img.url))
        admin_image.allow_tags = True

admin.site.register(Gallery, CustomAdmin)
