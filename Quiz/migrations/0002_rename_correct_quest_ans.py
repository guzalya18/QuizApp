# Generated by Django 4.1 on 2022-09-15 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quest',
            old_name='correct',
            new_name='ans',
        ),
    ]