# Generated by Django 4.2.11 on 2024-04-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_contactform_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.IntegerField(default=6000),
        ),
    ]