# Generated by Django 5.0.4 on 2024-04-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0005_alter_todo_days_alter_todo_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
