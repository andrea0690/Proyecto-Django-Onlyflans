# Generated by Django 4.2.11 on 2024-04-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='customer_name',
            field=models.CharField(max_length=30),
        ),
    ]