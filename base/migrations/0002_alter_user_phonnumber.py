# Generated by Django 3.2.18 on 2023-04-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonnumber',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
