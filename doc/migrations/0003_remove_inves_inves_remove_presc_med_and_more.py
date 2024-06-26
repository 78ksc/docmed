# Generated by Django 4.2.1 on 2023-11-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_investigation'),
        ('doc', '0002_docsuggest_presc_inves_docsuggest_investigations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inves',
            name='inves',
        ),
        migrations.RemoveField(
            model_name='presc',
            name='med',
        ),
        migrations.AlterField(
            model_name='docsuggest',
            name='investigations',
            field=models.ManyToManyField(related_name='investigations', to='med.investigation'),
        ),
        migrations.AlterField(
            model_name='docsuggest',
            name='prescriptions',
            field=models.ManyToManyField(related_name='prescriptions', to='med.medicen'),
        ),
    ]
