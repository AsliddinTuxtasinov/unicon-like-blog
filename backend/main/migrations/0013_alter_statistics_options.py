# Generated by Django 4.1.6 on 2023-02-15 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_statistics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name': 'Statistic', 'verbose_name_plural': 'Statistics'},
        ),
    ]