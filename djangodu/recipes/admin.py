
from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import RecipeIngredient, Recipe

User = get_user_model()
admin.site.unregister(User)

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0
    readonly_fields = ['quantity_as_float']


class UserAdmin(admin.ModelAdmin):
    inline = []
    list_display = ['username']

admin.site.register(User,UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    #fields = ['name', 'quanity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)