from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_merge_20230216_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationservice',
            name='info_cat',
            field=models.CharField(choices=[('NS', 'NEWS'), ('PR', 'PHOTO REPORT'), ('MM', 'MEMORANDUM'), ('oav', 'OAV ABOUT US'), ('VR', 'VIDEO REPORT')], max_length=3, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='itn',
            field=models.CharField(max_length=50, verbose_name='INN: '),
        ),
    ]
