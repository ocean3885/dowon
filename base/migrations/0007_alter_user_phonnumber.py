# Generated by Django 3.2.18 on 2023-04-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_submit_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonnumber',
            field=models.CharField(max_length=20, unique=True, verbose_name='전화번호'),
        ),
    ]
