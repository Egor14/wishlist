# Generated by Django 2.2.5 on 2019-09-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_auto_20190918_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='link',
            field=models.CharField(max_length=400),
        ),
    ]