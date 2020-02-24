from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'like_count','full_title']
    search_fields = ['title']

admin.site.register(Item, ItemAdmin)

Item.full_title