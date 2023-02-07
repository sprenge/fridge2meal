from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=80)
    plural = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    alias = models.CharField(max_length=256)
    is_food = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Qualifier(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Book(models.Model):
    BID = models.CharField(max_length=80, unique=True)
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=80)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Recipe(models.Model):
    RID = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=512)
    persons = models.IntegerField(default=2)
    page = models.IntegerField()
    preparation = models.IntegerField(
        blank=True, null=True, help_text="preparation time in minutes")
    cooking = models.IntegerField(
        blank=True, null=True, help_text="cooking time in minutes")
    energy = models.IntegerField(
        blank=True, null=True, help_text="total energy required in KWH")
    soak = models.IntegerField(
        blank=True, null=True, help_text="soak time in minutes")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.RID


class RecipeIngredient(models.Model):
    quantity = models.IntegerField(default=1)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qualifier = models.ForeignKey(Qualifier, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient + '_' + self.recipe
