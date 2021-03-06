from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

from .utils import number_str_to_float
from .validators import validate_unit_of_measure

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    quantity_as_float = models.FloatField(blank=True, null=True)
    # 'pounds', 'kg', 'oz', 'grams'
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure], blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
            qty = self.quantity
            qty_as_float, qty_as_float_success = number_str_to_float(qty)
            if qty_as_float_success:
                self.quantity_as_float = qty_as_float
            else:
                self.quantity_as_float = None
            super().save(*args, **kwargs)



#class RecipeImage():
#    recipe = models.ForeignKey(Recipe)