# Generated by Django 5.0.4 on 2024-04-27 15:33

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0004_alter_todo_done_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='days',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
