# Generated by Django 4.2.1 on 2023-11-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20231105_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='emergency',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
