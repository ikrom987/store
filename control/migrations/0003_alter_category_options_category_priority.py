# Generated by Django 4.0.1 on 2022-01-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-priority',)},
        ),
        migrations.AddField(
            model_name='category',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
