# Generated by Django 2.2.4 on 2019-08-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_films'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]