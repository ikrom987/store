# Generated by Django 4.0.1 on 2022-01-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_alter_category_options_category_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('priority',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('priority',)},
        ),
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]