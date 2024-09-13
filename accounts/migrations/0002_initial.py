# Generated by Django 5.1.1 on 2024-09-13 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.families'),
        ),
        migrations.AddField(
            model_name='institutions',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.families'),
        ),
    ]
