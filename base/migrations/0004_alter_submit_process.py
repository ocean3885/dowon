# Generated by Django 3.2.18 on 2023-04-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_submit_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='process',
            field=models.CharField(choices=[('입금대기', 'STEP1'), ('진행중', 'STEP2'), ('완료', 'STEP3')], max_length=20, null=True),
        ),
    ]
