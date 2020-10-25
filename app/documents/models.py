from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='profiles/images/', null=True, blank=True)
    is_partner = models.BooleanField()

    def __str__(self):
        return self.name


class Document(models.Model):
    class DocType(models.TextChoices):
        DOCUMENTO = 'DOC'
        PARTITURA = 'PAR'
        LIBRO = 'LIB'
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    authors = models.ManyToManyField(
        Author, default=2
    )
    type = models.CharField(
        max_length=3, choices=DocType.choices, default=DocType.DOCUMENTO)
    name = models.CharField(max_length=50)
    sumary = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    cover = models.ImageField(upload_to='images/', null=True)
    document = models.FileField(upload_to='documents/', null=True)
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
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    document = models.ForeignKey(
        Document, on_delete=models.SET_NULL, null=True, blank=True
    )
    free_download = models.BooleanField(default=True)
    downloads_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class DocumentDetail(models.Model):
    document = models.ForeignKey(
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
        OK = 'OK'
        DENIED = 'DN'
        CANCELLED = 'CN'
        REFOUNDED = 'RF'
    paypal_id = models.IntegerField()
    status = models.CharField(max_length=2, choices=StatusType.choices)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, null=True, blank=True
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True
    )
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.start_date)

    def save(self, *args, **kwargs):
        now = datetime.now()
        end = now + timedelta(31)
        self.start_date = now
        self.end_date = end
        return super(UserSubscription, self).save(*args, **kwargs)
