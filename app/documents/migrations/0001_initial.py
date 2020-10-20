# Generated by Django 3.1.2 on 2020-10-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DC', 'Documento'), ('PR', 'Partitura'), ('LB', 'Libro')], default='DC', max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('sumary', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1024)),
                ('is_active', models.BooleanField()),
                ('is_premium', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('premium_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
