# Generated by Django 2.1.1 on 2019-08-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestSummary', '0003_testsummary_testitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsummary',
            name='testitem',
            field=models.CharField(default='', max_length=500),
        ),
    ]
