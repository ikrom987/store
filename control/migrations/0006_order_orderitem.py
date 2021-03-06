# Generated by Django 4.0.1 on 2022-01-31 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('transaction', models.CharField(blank=True, max_length=255, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.account')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.product')),
            ],
        ),
    ]
