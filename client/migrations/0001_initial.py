# Generated by Django 3.2.18 on 2023-11-05 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('pincode', models.IntegerField(blank=True)),
                ('area', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacient_name', models.CharField(max_length=40)),
                ('pacient_age', models.IntegerField()),
                ('pacient_addr', models.CharField(max_length=200)),
                ('doctor_spec', models.CharField(blank=True, max_length=120)),
                ('pacient_symptom', models.CharField(max_length=240)),
                ('emergency', models.BooleanField(default=False)),
                ('alloted_docto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doc.doctor')),
                ('request_created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
            ],
        ),
    ]
