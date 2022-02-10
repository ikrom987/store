# Generated by Django 4.0.1 on 2022-01-21 12:01

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image_min', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[250, 250], upload_to='products/')),
                ('image_max', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[600, 600], upload_to='products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.category')),
            ],
        ),
    ]