# Generated by Django 2.1.7 on 2020-02-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteuser',
            name='DOB',
            field=models.DateField(null=True),
        ),
    ]
