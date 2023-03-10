# Generated by Django 4.1.6 on 2023-02-08 07:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_status', models.CharField(choices=[('CS', 'KONKURSLAR'), ('IK', 'TAKLIFLAR_TANLOVI')], max_length=2)),
                ('status_type', models.CharField(choices=[('CS', 'OZ_KUCHIDA'), ('IK', 'MUDDATI_TUGAGAN')], max_length=2)),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': "E'lon",
                'verbose_name_plural': "E'lonlar",
            },
        ),
        migrations.CreateModel(
            name='InformationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_cat', models.CharField(choices=[('NS', 'YANGILIKLAR'), ('PR', 'FOTO REPORTAJ'), ('VR', 'VIDEO REPORTAJ')], max_length=2)),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Axborat xizmati',
                'verbose_name_plural': 'Axborat xizmatlari',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_type', models.CharField(choices=[('RT', 'RAXBARIYAT'), ('IK', 'ILMIY KENGASH'), ('BJ', 'BIZNING JAMOA')], max_length=2)),
                ('image', models.ImageField(upload_to='content/member-image')),
                ('full_name', models.CharField(max_length=255)),
                ('full_name_uz', models.CharField(max_length=255, null=True)),
                ('full_name_ru', models.CharField(max_length=255, null=True)),
                ('department', models.CharField(max_length=255)),
                ('department_uz', models.CharField(max_length=255, null=True)),
                ('department_ru', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('icon', models.ImageField(upload_to='content/nav-about-product-icon')),
                ('img', models.ImageField(blank=True, null=True, upload_to='content/nav-about-product-img')),
                ('content', ckeditor.fields.RichTextField()),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
            ],
            options={
                'verbose_name': 'Maxsulot',
                'verbose_name_plural': 'Maxsulotlar',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('short_desc', models.CharField(max_length=255)),
                ('short_desc_uz', models.CharField(max_length=255, null=True)),
                ('short_desc_ru', models.CharField(max_length=255, null=True)),
                ('icon', models.ImageField(upload_to='content/nav-about-resource-icon')),
            ],
            options={
                'verbose_name': 'Resurs',
                'verbose_name_plural': 'Resurslar',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Xizmat',
                'verbose_name_plural': 'Xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='ResourceContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('short_desc', models.CharField(max_length=255)),
                ('short_desc_uz', models.CharField(max_length=255, null=True)),
                ('short_desc_ru', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(upload_to='content/resource-content-file')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_content', to='main.resource')),
            ],
            options={
                'verbose_name': 'Resurs conteni',
                'verbose_name_plural': 'Resurs contentlari',
            },
        ),
        migrations.CreateModel(
            name='EmailMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='file-message/')),
                ('is_agree', models.BooleanField()),
                ('created_add', models.DateField(auto_now_add=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.services')),
            ],
            options={
                'verbose_name': 'Email xabari',
                'verbose_name_plural': 'Email xabarlar',
            },
        ),
        migrations.CreateModel(
            name='ContentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='content/content-images')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_images', to='main.informationservice')),
            ],
        ),
    ]
