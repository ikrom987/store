# Generated by Django 3.2.7 on 2022-02-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
