from django.contrib import admin
from . import models


admin.site.register(models.Document)
admin.site.register(models.Category)
admin.site.register(models.Download)
admin.site.register(models.DocumentDetail)
admin.site.register(models.Subscription)
admin.site.register(models.Payment)
admin.site.register(models.UserSubscription)
admin.site.register(models.Author)
