# Generated by Django 3.0 on 2019-12-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsh_scrapper', '0003_auto_20191216_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
