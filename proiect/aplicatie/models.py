from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    active = models.BooleanField(default=True)

    # subcat = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    # subcategories = []

    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        return f'{self.name}'


class Subcategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    models.BooleanField(default=True)

    # subcategories = []

    # Transactions
    # id = 1 subcategory_id = 1
    # id = 2 subcategory_id = 2
    #
    # Subcategory
    # id = 1 category_id = 1
    # id = 2 category_id = 3
    #
    # Category
    # id = 1 nume = cheltuieli_masina
    # id = 2 nume = cheltuieli_casa
    # id = 3 nume = cheltuieli_curs
    #

    def __str__(self):
        return f'{self.name}'


class Transactions(models.Model):
    date = models.DateTimeField(null=True)
    account = models.CharField(max_length=300)
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
    )
    amount = models.FloatField()
    note = models.CharField(max_length=300)
    type = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date} --> {self.amount}'


class Logs(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'update'),
                      ('refresh', 'refresh'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
