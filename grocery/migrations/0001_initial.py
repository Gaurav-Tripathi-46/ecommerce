# Generated by Django 5.1.4 on 2025-01-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('quantity', models.CharField(max_length=50)),
            ],
        ),
    ]
