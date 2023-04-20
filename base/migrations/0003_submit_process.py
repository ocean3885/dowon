# Generated by Django 3.2.18 on 2023-04-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_phonnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='process',
            field=models.CharField(choices=[('입금대기', 'STEP1'), ('진행중', 'STEP2'), ('완료', 'STEP3')], default=2, max_length=20),
            preserve_default=False,
        ),
    ]
