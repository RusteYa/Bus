# Generated by Django 3.0 on 2019-12-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Marsh',
            field=models.CharField(max_length=10),
        ),
    ]