from django.contrib import admin
from . models import Article
from . models import Category, Owner, Donation, Gdpr, Scripts, Join
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, CustomAdmin)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Donation)
admin.site.register(Gdpr)
admin.site.register(Scripts)
admin.site.register(Join)