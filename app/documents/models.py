from django.db import models


class Document(models.Model):
    class DocType(models.TextChoices):
        DOCUMENTO = 'DC'
        PARTITURA = 'PR'
        LIBRO = 'LB'
    # user_id
    type = models.CharField(
        max_length=2, choices=DocType.choices, default=DocType.DOCUMENTO)
    name = models.CharField(max_length=50)
    sumary = models.CharField(max_length=250)
    description = models.CharField(max_length=1024)
    # cover
    # file
    # partial_file
    is_active = models.BooleanField()
    is_premium = models.BooleanField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    premium_price = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
