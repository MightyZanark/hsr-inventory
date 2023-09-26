from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.TextField()

    CHAREXP = "CHAR_EXP"
    LCEXP = "LC_EXP"
    RELEXP = "RELIC_EXP"
    CATEGORY_CHOICES = [
        (CHAREXP, "Character EXP Material"),
        (LCEXP, "Light Cone EXP Material"),
        (RELEXP, "Relic Exp Material"),
    ]
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default=CHAREXP)
