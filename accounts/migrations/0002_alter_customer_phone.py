# Generated by Django 3.2.3 on 2021-10-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
