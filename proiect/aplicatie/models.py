from django.db import models

# Create your models here.


class Transactions(models.Model):
    # account_choices = (('created', 'created'),
    #                    ('updated', 'update'),
    #                    ('refresh', 'refresh'))

    date = models.DateTimeField(null=True)
    # account = models.CharField(max_length=10, choices=account_choices)
    account = models.CharField(max_length=300)
    amount = models.FloatField()
    note = models.CharField(max_length=300)
    type = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} --> {self.amount}'

