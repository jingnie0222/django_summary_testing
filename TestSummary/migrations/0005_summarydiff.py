# Generated by Django 2.1.1 on 2019-09-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestSummary', '0004_auto_20190808_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryDiff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default=0)),
                ('storage_time', models.CharField(default='', max_length=50)),
                ('base_res', models.TextField(default='')),
                ('test_res', models.TextField(default='')),
            ],
        ),
    ]
