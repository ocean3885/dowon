# Generated by Django 3.2.18 on 2023-04-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manseryuk', '0009_manseryuk_yd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manseryuk',
            name='day',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='manseryuk',
            name='month',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='manseryuk',
            name='yd',
            field=models.CharField(choices=[(0, '평달'), (1, '윤달')], default=0, max_length=10, null=True),
        ),
    ]
