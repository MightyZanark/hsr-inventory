from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.TextField()

    CHAREXP = "CHAREXP"
    LCEXP = "LCEXP"
    RELEXP = "RELEXP"
    CATEGORY_CHOICES = [
        (CHAREXP, "Character EXP Material"),
        (LCEXP, "Light Cone EXP Material"),
        (RELEXP, "Relic Exp Material"),
    ]
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES, default=CHAREXP)
