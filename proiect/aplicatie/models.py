from django.db import models


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=300)
#     subcategory = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
#     subcategories = []
#     pass
#
#
# class Subcategory(models.Model):
#     name = models.CharField(max_length=300)
#     category = models.ForeignKey(Category, null=True, on_delete=models.set_null)
#     subcategories = []


class Transactions(models.Model):

    date = models.DateTimeField(null=True)
    account = models.CharField(max_length=300)
    # category = models.OneToOneField(
    #     Category,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
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



