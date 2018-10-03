from django.contrib import admin

from .models import (
    Game,
    Item,
    ItemVersion,
    Patch,
)
# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('title',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('name',)

@admin.register(ItemVersion)
class ItemVersionAdmin(admin.ModelAdmin):
    pass

@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    pass