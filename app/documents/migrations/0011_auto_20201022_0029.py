# Generated by Django 3.1.2 on 2020-10-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_auto_20201022_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paypal',
            new_name='paypal_id',
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(null=True, upload_to='profiles/images/'),
        ),
        migrations.AddField(
            model_name='document',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]