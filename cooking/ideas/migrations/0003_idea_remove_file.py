# Generated by Django 3.2.4 on 2021-09-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='remove_file',
            field=models.BooleanField(default=False),
        ),
    ]