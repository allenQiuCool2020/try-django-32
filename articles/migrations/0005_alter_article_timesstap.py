# Generated by Django 3.2.18 on 2023-07-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20230709_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='timesstap',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]