# Generated by Django 4.1.6 on 2023-02-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_emailmessages_created_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessages',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
