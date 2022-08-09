from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Menu, Event, Galery, WhytUs, AboutUs, Spesial

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(AboutUs)
admin.site.register(Event)
admin.site.register(Galery)
admin.site.register(WhytUs)
admin.site.register(Spesial)

