# Generated by Django 3.2.18 on 2023-03-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manseryuk', '0007_auto_20230329_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manseryuk',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
