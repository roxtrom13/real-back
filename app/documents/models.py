from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    class DocType(models.TextChoices):
        DOCUMENTO = 'DC'
        PARTITURA = 'PR'
        LIBRO = 'LB'
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    type = models.CharField(
        max_length=2, choices=DocType.choices, default=DocType.DOCUMENTO)
    name = models.CharField(max_length=50)
    sumary = models.CharField(max_length=255)
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
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Download(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    document_id = models.ForeignKey(
        Document, on_delete=models.SET_NULL, null=True, blank=True
    )
    free_download = models.BooleanField()
    downloads_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class DocumentDetail(models.Model):
    document_id = models.ForeignKey(
        Document, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    class StatusType(models.TextChoices):
        IDK = 'DK'
        WTF = 'WT'
        XD = 'XD'
    paypal_id = models.IntegerField()
    status = models.CharField(max_length=2, choices=StatusType.choices)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class UserSubscription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, null=True, blank=True
    )
    subscription_id = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True
    )
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # end_date = models.DateTimeField(blank=True, null=True) HELP

    def __str__(self):
        return str(self.start_date)
