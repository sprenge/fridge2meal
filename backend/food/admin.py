from django.contrib import admin
from food.models import Unit, Ingredient, Qualifier, Book
from food.models import RecipeIngredient, Recipe


class UnitAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class QualifierAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class RecipeIngredientAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Qualifier, QualifierAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
