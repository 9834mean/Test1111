# Generated by Django 3.1.3 on 2024-03-11 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='create_data',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
