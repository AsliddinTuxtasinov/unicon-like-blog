# Generated by Django 4.1.6 on 2023-02-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_contentadditionalfiles_is_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='emailmessages',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
